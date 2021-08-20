class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(result)
        if max((len(w) for w in words)) > n:
            return False
        level = [[w[-k - 1] for w in words if k < len(w)] for k in range(n)]
        level_set = [set(level[k]) | {result[-k - 1]} for k in range(n)]
        leading = set((w[0] for w in words)) | {result[0]}
        val = {k: None for k in set.union(set(result), *(set(w) for w in words))}
        used = set()

        def search(k, carry):
            if k == n:
                return carry == 0
            for c in level_set[k]:
                if val[c] is None:
                    for v in range(c in leading, 10):
                        if v not in used:
                            val[c] = v
                            used.add(v)
                            if search(k, carry):
                                return True
                            val[c] = None
                            used.remove(v)
                    return False
            s = sum((val[c] for c in level[k])) + carry
            if s % 10 != val[result[-k - 1]]:
                return False
            return search(k + 1, s // 10)
        return search(0, 0)
