class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        spans = [(1, N)]
        step = N

        if m == N:
            return m

        while arr:
            #print(step, spans)
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
