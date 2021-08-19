class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def next_permutation(a):
            for i in range(len(a) - 1, 0, -1):
                if a[i] > a[i - 1]:
                    ps = i
                    for j in range(i + 1, len(a)):
                        if a[j] > a[i - 1] and a[ps] > a[j]:
                            ps = j
                    (a[ps], a[i - 1]) = (a[i - 1], a[ps])
                    p1 = i
                    p2 = len(a) - 1
                    while p1 < p2:
                        (a[p1], a[p2]) = (a[p2], a[p1])
                        p1 += 1
                        p2 -= 1
                    return True
            return False
        n = 1
        for i in range(1, len(tiles) + 1):
            n *= i
        a = set()
        perm = []
        for i in range(len(tiles)):
            perm.append(i)
        for _ in range(n):
            cur = ''
            for i in range(len(tiles)):
                cur += tiles[perm[i]]
            for i in range(len(tiles)):
                a.add(cur[:i + 1])
            next_permutation(perm)
        return len(a)
