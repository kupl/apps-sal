class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        csum = [0]
        for a in A:
            csum.append(csum[-1] + a)
        counter = collections.Counter()
        ans = 0
        print(csum)
        for p in csum:
            ans += counter[p - S]
            # print('with',p,'found',counter[p-S],p-S)
            counter[p] += 1
        return ans
