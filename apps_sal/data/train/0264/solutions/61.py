class Solution:

    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for word in arr:
            if len(word) != len(set(word)):
                continue
            curWord = set(word)
            for used in dp[:]:
                if len(used & curWord) == 0:
                    dp.append(used | curWord)
        return len(max(dp, key=len))
