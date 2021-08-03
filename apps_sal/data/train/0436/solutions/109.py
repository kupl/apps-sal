class Solution:
    def minDays(self, n: int) -> int:
        cache = {n: 1}
        q = [n]
        level = 0
        while q:
            _q = []
            for val in q:
                if val == 0:
                    return level

                _val = val - 1
                if _val not in cache and _val >= 0:
                    cache[_val] = 1
                    _q.append(_val)

                _val = val - val // 2
                if _val not in cache and val % 2 == 0 and _val >= 0:
                    cache[_val] = 1
                    _q.append(_val)

                _val = val - (2 * val) // 3
                if _val not in cache and val % 3 == 0 and _val >= 0:
                    cache[_val] = 1
                    _q.append(_val)
            q = _q
            level += 1
        return -1
