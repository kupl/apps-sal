class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        MOD = 7 + 1e9

        @lru_cache(maxsize=None)
        def helper(step, char):
            if step == n:
                return 1

            result = 0
            if step == 0:
                for currChar in vowels:
                    result = (result + helper(step + 1, currChar)) % MOD
            else:
                if char == 'a':
                    result = (result + helper(step + 1, 'e')) % MOD
                elif char == 'e':
                    result = (result + helper(step + 1, 'a')) % MOD
                    result = (result + helper(step + 1, 'i')) % MOD
                elif char == 'i':
                    for currChar in vowels:
                        if currChar == 'i':
                            continue
                        result = (result + helper(step + 1, currChar)) % MOD
                elif char == 'o':
                    result = (result + helper(step + 1, 'i')) % MOD
                    result = (result + helper(step + 1, 'u')) % MOD
                elif char == 'u':
                    result = (result + helper(step + 1, 'a')) % MOD
            return result
        return int(helper(0, ''))
