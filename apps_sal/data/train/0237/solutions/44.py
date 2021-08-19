class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        cumsum = 0
        dic = {0: [-1]}
        ans = 0
        for (i, num) in enumerate(A):
            cumsum += num
            dic[cumsum] = dic.get(cumsum, []) + [i]
            ans += len(dic.get(cumsum - S, []))
        return ans - (0 if S else len(A))
