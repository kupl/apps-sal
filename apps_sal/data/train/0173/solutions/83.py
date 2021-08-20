class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        modulo_map = defaultdict(lambda: [])
        pairs = []
        for a in arr:
            r = k - a % k if a % k != 0 else 0
            if r in list(modulo_map.keys()) and len(modulo_map[r]) > 0:
                pairs.append((a, modulo_map[r].pop(-1)))
                if len(modulo_map[r]) == 0:
                    del modulo_map[r]
            else:
                modulo_map[a % k].append(a)
        if len(pairs) == n // 2:
            return True
        else:
            return False
