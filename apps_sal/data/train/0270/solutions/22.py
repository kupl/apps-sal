class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        results = []
        letters = 'abc'
        combos = set()

        def backtrack(s):
            nonlocal results
            if len(results) == k:
                return
            if len(s) == n and s not in combos:
                combos.add(s)
                results.append(s)
                return
            for i in range(0, len(letters)):
                if s and s[-1] == letters[i]:
                    continue
                s += letters[i]
                backtrack(s)
                s = s[0:-1]

        backtrack('')
        return results[-1] if len(results) == k else ''
