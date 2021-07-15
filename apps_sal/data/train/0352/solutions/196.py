def predecessor(word, candidate):
    if len(word) != len(candidate)+1:
        return False
    j = 0
    for i, c in enumerate(word):
        if i > j + 1 or j == len(candidate):
            break
        if c == candidate[j]:
            j += 1
    return j == len(candidate)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = [1 for _ in words]
        for start in range(len(words)):
            for end in range(start-1, -1, -1):
                if len(words[end]) < len(words[start])-1:
                    break
                if predecessor(words[start], words[end]):
                    dp[start] = max(dp[start], 1 + dp[end])
        return max(dp)
