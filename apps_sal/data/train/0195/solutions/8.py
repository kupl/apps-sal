class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        count = 0
        dic = collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                dic[(A[i] & A[j])] += 1
        ans = 0
     #   print(dic)
        for ele in A:
            for res in dic:
                if res & ele == 0:
                    ans += dic[res]

        return ans
