class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        A = list(A)
        B = list(B)

        n = len(A)

        # ans = 0
        # for i in range(n):
        #     if A[i]==B[i]:
        #         continue
        #     else:
        #         ans+=1
        #         for j in range(i+1, n):
        #             if B[j] == A[i]:
        #                 B[i], B[j] = B[j], B[i]
        #                 break
        # return ans

        def rec(i):
            if i == n:
                return 0

            if A[i] == B[i]:
                return rec(i + 1)
            else:
                min_ = sys.maxsize
                for j in range(i + 1, n):
                    if B[j] == A[i] and B[j] != A[j]:
                        B[i], B[j] = B[j], B[i]
                        min_ = min(min_, rec(i + 1) + 1)
                        B[i], B[j] = B[j], B[i]
                return min_

        return rec(0)


#         ans = 0
#         for i in range(n):
#             if A[i]==B[i]:
#                 continue
#             else:
#                 ans+=1
#                 for j in range(i+1, n):
#                     if B[j] == A[i] and B[j]!=A[j]:
#                         B[i], B[j] = B[j], B[i]
#                         break
#         return ans


#         def rec(i):
#             if i==n:
#                 return 0

#             if A[i]==B[i]:
#                 return rec(i+1)
#             else:
#                 min_ = sys.maxsize
#                 j = 0
#                 while A[j]==B[j]:
#                     j+=1
#                 for k in range(j+1, n):
#                     if B[k] == A[j]:
#                         B[j], B[k] = B[k], B[j]
#                         min_ = min(min_, rec(i+1) + 1)
#                         B[j], B[k] = B[k], B[j]
#                 return min_

#         return rec(0)
#         def nei(x):
#             i = 0
#             while x[i] == B[i]: i+=1
#             for j in range(i+1, len(x)):
#                 if x[j] == B[i]: yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
#         q, seen = [(A,0)], set([A])

#         for x, d in q:
#             if x == B: return d
#             for y in nei(x):
#                 if y not in seen:
#                     seen.add(y), q.append((y,d+1))
