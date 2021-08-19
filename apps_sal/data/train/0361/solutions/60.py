class Solution:
    def tilingRectangle(self, R, C):
        A = [[0] * C for _ in range(R)]
        self.ans = R * C

        def search(r, c, steps):
            if steps >= self.ans:
                return
            if r == R:
                self.ans = steps
                return
            if c == C:
                return search(r + 1, 0, steps)
            if A[r][c]:
                return search(r, c + 1, steps)

            # A[r][c] is empty
            for k in range(min(R - r, C - c), 0, -1):
                # If A[r:r+k][c:c+k] is empty:
                bad = False
                for r0 in range(r, r + k):
                    for c0 in range(c, c + k):
                        if A[r0][c0]:
                            bad = True
                            break
                    if bad:
                        break

                if not bad:
                    for r0 in range(r, r + k):
                        for c0 in range(c, c + k):
                            A[r0][c0] = 1

                    search(r, c + 1, steps + 1)
                    for r0 in range(r, r + k):
                        for c0 in range(c, c + k):
                            A[r0][c0] = 0

        search(0, 0, 0)
        return self.ans
