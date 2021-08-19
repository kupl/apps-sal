class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        pool, c, repeat = [], max(set(s)), False    # c is the max char, pool contains the candidates
        for i, x in enumerate(s):
            if x == c:
                if not repeat:                      # only add non-repeat head (if there's some smaller char in between) 'zzzazz...', not add 'zzzzzz...'
                    pool.append(i)
                    repeat = True
            else:
                repeat = False
        k = 1
        while len(pool) > 1:                        # if there are more than one substring start with the head
            new_pool, c = [], ''
            for i in pool:
                sc = s[i + k] if i + k < n else ''      # continue to compare the second, third, ..., k-th char
                if sc > c:
                    new_pool = [i]
                    c = sc
                elif sc == c:
                    new_pool.append(i)
            pool = new_pool
            k += 1                                  # compare the next char
        return s[pool[0]:]
