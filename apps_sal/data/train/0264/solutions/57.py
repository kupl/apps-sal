class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        length = 0
        for word in arr:
            if len(word) != len(set(word)):
                continue
            curr = set(word)
            for used in dp[:]:
                if not len(used & curr):
                    dp.append(used | curr)
                    length = max(length, len(used | curr))
        return length
