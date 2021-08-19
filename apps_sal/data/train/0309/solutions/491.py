class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        cnt
        arith = [Counter() for i in range(len(A))]
        for i in range(len(A) - 2, -1, -1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                arith[i][diff] = max(1 + arith[j][diff], arith[i][diff])
        # print(arith)
        longest = 0
        for i in range(len(A)):
            # print(arith[i])
            most_common = arith[i].most_common()

            longest = max(most_common[0][1] if most_common else 0, longest)
        return longest + 1
        # for i in range(len(A)):
        #     for j in range(i+1, len(A)):
        #         cnt[A[j]-A[i]] += 1
        #     print(A[i], cnt)
        # print(cnt)
        # val = cnt.most_common()[0][1]
        # return val + 1


#         self.arith = [dict() for i in range(len(A))]

#         def helper(i, diff):
#             if diff in self.arith[i]:
#                 return self.arith[i][diff]

#             val = 0
#             for j in range(i+1, len(A)):
#                 if A[j] - A[i] == diff:
#                     val = 1 + helper(j, diff)
#                     break
#             self.arith[i][diff] = val
#             return self.arith[i][diff]
