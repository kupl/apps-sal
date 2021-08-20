class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        numToFreq = {}
        numToFreq[0] = 1
        now_sum = 0
        ans = 0
        for num in A:
            now_sum += num
            if now_sum == S:
                ans += numToFreq[0]
            elif now_sum > S:
                if now_sum - S in numToFreq:
                    ans += numToFreq[now_sum - S]
            if now_sum not in numToFreq:
                numToFreq[now_sum] = 0
            numToFreq[now_sum] += 1
        return ans
