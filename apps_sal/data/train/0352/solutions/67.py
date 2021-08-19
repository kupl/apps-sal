class Solution:

    def IsPredecessor(self, w1, w2):
        if len(w1) + 1 != len(w2):
            return False
        if len(w1) == 0:
            return True
        diff = 0
        for i in range(len(w2)):
            if i - diff == len(w1) or w1[i - diff] != w2[i]:
                diff += 1
        return diff == 1

    def longestStrChain(self, words: List[str]) -> int:
        if len(words) < 1:
            return 0
        length_position = {}
        for i in range(len(words)):
            w = words[i]
            if len(w) in length_position:
                length_position[len(w)].append(i)
            else:
                length_position[len(w)] = [i]
        dp = [1] * len(words)
        for i in sorted(length_position):
            if i - 1 not in length_position:
                continue
            current = length_position[i]
            previous = length_position[i - 1]
            for j in current:
                for k in previous:
                    if self.IsPredecessor(words[k], words[j]):
                        dp[j] = max(dp[j], dp[k] + 1)
        return max(dp)
