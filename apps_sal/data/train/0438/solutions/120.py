class Solution:
    def findLatestStep2(self, arr: List[int], m: int) -> int:
        N = len(arr)
        spans = [(1, N)]
        step = N

        if m == N:
            return m

        while arr:
            d = arr.pop()
            step -= 1
            for span in spans:
                if span[0] <= d <= span[1]:
                    if d - span[0] == m or span[1] - d == m:
                        return step

                    spans.remove(span)
                    if d - span[0] > m:
                        spans.append((span[0], d - 1))
                    if span[1] - d > m:
                        spans.append((d + 1, span[1]))

        return -1

    def findLatestStep(self, A, m):
        if m == len(A):
            return m
        length = [0] * (len(A) + 2)
        res = -1
        for i, a in enumerate(A):
            left, right = length[a - 1], length[a + 1]
            if left == m or right == m:
                res = i
            length[a - left] = length[a + right] = left + right + 1
        return res
