class Solution:

    @lru_cache(None)
    def countVowelPermutation(self, n: int) -> int:
        prevs = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for i in range(1, n):
            cur = defaultdict(int)
            for (prev, count) in prevs.items():
                if prev == 'a':
                    cur['e'] += count
                elif prev == 'e':
                    for nextch in ['a', 'i']:
                        cur[nextch] += count
                elif prev == 'i':
                    for nextch in ['a', 'e', 'o', 'u']:
                        cur[nextch] += count
                elif prev == 'o':
                    for nextch in ['i', 'u']:
                        cur[nextch] += count
                elif prev == 'u':
                    cur['a'] += count
            prevs = cur
        return sum(prevs.values()) % 1000000007
        '\n        vocals = [\'aeiou\']\n        arr = vocals * n\n        prods = list(map("".join, itertools.product(*arr)))\n        count = 0\n        for prod in prods:\n            if "aa" in prod or "ai" in prod or "ao" in prod or "au" in prod or "ee" in prod or "eo" in prod or "eu" in prod or "ii" in prod or "oa" in prod or "oe" in prod or "oo" in prod or "ue" in prod or "ui" in prod or "uo" in prod or "uu" in prod:\n                continue\n            print(prod)\n            count += 1\n        return count%(10**9+7)\n        '
