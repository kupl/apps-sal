class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        N = len(tree)
        out = 0
        start = 0
        olderstart = 0
        newerend = newerstart = 0
        olderend = olderstart = 0
        older = newer = tree[0]
        j = 0
        if N < 3:
            return len(tree)
        while newer == older and j < N:
            olderend = j
            j += 1
            if j == N:
                return N
            newer = tree[j]
            newerstart = j

        assert(newer != older)

        for i in range(j, N):
            curr = tree[i]
            if (curr == older or curr == newer):
                if curr == older:
                    olderend = i
                if curr == newer:
                    newerend = i

            else:

                if prev == older:
                    olderstart = newerend + 1
                else:
                    olderstart = olderend + 1
                    olderend = newerend
                    older = newer

                newerstart = i
                newerend = i
                newer = curr

            prev = curr
            out = max(i - olderstart + 1, out)
        return out
