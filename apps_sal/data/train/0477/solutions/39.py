class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        from copy import deepcopy

        @lru_cache()
        def help(i):
            if i == 1:
                return '0'

            s = help(i - 1)
            s2 = deepcopy(s)
            v = []
            for i in s:
                v.append(i)

            for i in range(len(v)):
                if v[i] == '1':
                    v[i] = '0'

                else:
                    v[i] = '1'

            v = v[::-1]
            s = ''.join(v)
            return s2 + '1' + s

        return help(n)[k - 1]
