class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        temp = defaultdict(lambda: 0)
        for i in range(k):
            temp[s[i]] += 1
        ans = sum((temp[i] for i in 'aeiou'))
        for i in range(k, len(s)):
            temp[s[i - k]] -= 1
            temp[s[i]] += 1
            ans = max(ans, sum((temp[i] for i in 'aeiou')))
        return ans
