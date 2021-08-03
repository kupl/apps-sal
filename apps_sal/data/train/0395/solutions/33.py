class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        from sortedcontainers import SortedDict
        a = len(A)
        sd = SortedDict()
        sd[A[-1]] = [a - 1]

        odd = [0] * a
        even = [0] * a
        odd[-1] = even[-1] = 1

        for i in range(a - 2, -1, -1):
            n = A[i]
            right = left = sd.bisect_left(n)
            if left == len(sd) or sd.keys()[left] != n:
                left -= 1

            if left >= 0:
                even[i] = odd[sd.values()[left][-1]]
            if right < len(sd):
                odd[i] = even[sd.values()[right][-1]]

            if n in sd:
                sd[n].append(i)
            else:
                sd[n] = [i]

        return sum(odd)
