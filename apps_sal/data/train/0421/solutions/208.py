class Solution:

    def lastSubstring(self, s: str) -> str:
        n = len(s)
        (pool, c, repeat) = ([], max(set(s)), False)
        for (i, x) in enumerate(s):
            if x == c:
                if not repeat:
                    pool.append(i)
                    repeat = True
            else:
                repeat = False
        k = 1
        while len(pool) > 1:
            (new_pool, c) = ([], '')
            for i in pool:
                sc = s[i + k] if i + k < n else ''
                if sc > c:
                    new_pool = [i]
                    c = sc
                elif sc == c:
                    new_pool.append(i)
            pool = new_pool
            k += 1
        return s[pool[0]:]
