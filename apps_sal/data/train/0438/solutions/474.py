from collections import deque


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        pieces = {}
        goodpieces = {}
        latest = -1
        for i in range(1, len(arr) + 1):
            n = arr[i - 1]
            start, end = 0, 0
            if n + 1 in pieces and n - 1 in pieces:
                start = pieces.pop(n - 1)
                end = pieces.pop(n + 1)
            elif n + 1 in pieces:
                start = n
                end = pieces.pop(n + 1)
            elif n - 1 in pieces:
                start = pieces.pop(n - 1)
                end = n
            else:
                start = n
                end = n
            if (end - start + 1) == m:
                goodpieces[start] = end
            pieces[start] = end
            pieces[end] = start
            bad = []
            for piece in goodpieces:
                if (piece in pieces) and pieces[piece] == goodpieces[piece]:
                    latest = i
                else:
                    bad.append(piece)
            for b in bad:
                del goodpieces[b]

            # print(pieces)
        return latest
