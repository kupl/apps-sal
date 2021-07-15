class Solution:
    def distinctSubseqII(self, S: str) -> int:
        cache = {}
        extras = []
        
        module = 10 ** 9 + 7
        _sum = 0
        for i, s in enumerate(S):
            if i == 0:
                _sum += 1
                extras.append(1)
            else:
                prev_indexes = cache.setdefault(s, [])
                if not prev_indexes:
                    extras.append(_sum + 1)
                    _sum += (_sum + 1)
                else:
                    duplicated = sum([extras[j] for j in prev_indexes])
                    extras.append(_sum + 1 - duplicated)
                    
                    _sum += _sum + 1 - duplicated
            cache.setdefault(s, []).append(i)
        return _sum % (module)
