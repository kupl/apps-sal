from bisect import bisect_left


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        if m == N:
            return m
        bits = [(1, N)]
        ans = 0
        for i in range(N - 1, -1, -1):
            a = arr[i]
            idx = bisect_left(bits, (a, a))
            if idx < len(bits) and bits[idx][0] == a:
                if bits[idx][1] == a:
                    bits.pop(idx)
                else:
                    s, e = bits[idx]
                    if (e - s) == m:
                        return i
                    bits[idx] = (s + 1, e)
                continue
            idx -= 1
            if bits[idx][1] == a:
                bits[idx] = (bits[idx][0], a - 1)
                if bits[idx][1] - bits[idx][0] + 1 == m:
                    return i
            else:
                before = (bits[idx][0], a - 1)
                after = (a + 1, bits[idx][1])
                if (before[1] - before[0] + 1) == m:
                    return i
                if (after[1] - after[0] + 1) == m:
                    return i
                bits[idx:idx + 1] = [before, after]
        return -1
