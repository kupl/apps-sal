class Solution:

    def countVowelPermutation(self, n: int) -> int:

        def count(i, v, mem):
            key = (i, v)
            if key in mem:
                return mem[key]
            if i == n - 1:
                mem[key] = 1
                return mem[key]
            ans = 0
            if v == 'a':
                ans += count(i + 1, 'e', mem)
            elif v == 'e':
                ans += count(i + 1, 'a', mem)
                ans += count(i + 1, 'i', mem)
            elif v == 'i':
                ans += count(i + 1, 'a', mem)
                ans += count(i + 1, 'e', mem)
                ans += count(i + 1, 'o', mem)
                ans += count(i + 1, 'u', mem)
            elif v == 'o':
                ans += count(i + 1, 'i', mem)
                ans += count(i + 1, 'u', mem)
            elif v == 'u':
                ans += count(i + 1, 'a', mem)
            mem[key] = ans % (10 ** 9 + 7)
            return mem[key]
        mem = {}
        ans = count(0, 'a', mem) + count(0, 'e', mem) + count(0, 'i', mem) + count(0, 'o', mem) + count(0, 'u', mem)
        return ans % (10 ** 9 + 7)
