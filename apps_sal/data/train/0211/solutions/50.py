class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0

        cache = [None] * len(s)

        setSet = (self.dp(s, 0, cache))
        return len(max(setSet, key=lambda x: len(x))) if setSet else 0

    def dp(self, inputStr, i, cache):
        if i == len(inputStr):
            return [set()]

        if cache[i] is not None:
            return cache[i]

        end = len(inputStr) + 1

        res = set()
        for j in range(i + 1, end):
            tempSol = self.dp(inputStr, j, cache)

            for substrArr in tempSol:
                if inputStr[i:j] in substrArr:
                    continue

                combined = set(substrArr)
                combined.add(inputStr[i:j])
                res.add(frozenset(combined))

        cache[i] = frozenset(res)
        return cache[i]
