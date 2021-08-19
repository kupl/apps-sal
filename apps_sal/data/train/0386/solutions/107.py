class Solution:

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
