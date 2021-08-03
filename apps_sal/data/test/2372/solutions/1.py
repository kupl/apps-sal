from collections import deque


def main():

    def bfs(h1, w1, dp):
        """
        -1 - unsearched
        -2 - candidate for warp
        -3 - wall '#'
        """
        queue = deque()
        queue_warp = deque()
        queue.append([h1, w1])
        now = 0

        while queue:
            h1, w1 = queue.popleft()
            fl_up = False
            fl_left = False
            fl_down = False
            fl_right = False

            if h1 > 0:
                if dp[h1 - 1][w1] == -1 or dp[h1 - 1][w1] == -2:
                    if m[h1 - 1][w1] == '.':
                        dp[h1 - 1][w1] = now
                        queue.append([h1 - 1, w1])
                    else:
                        dp[h1 - 1][w1] = -3
                if dp[h1 - 1][w1] == -3:
                    fl_up = True
                    if h1 > 1:
                        if dp[h1 - 2][w1] == -1:
                            if m[h1 - 2][w1] == '.':
                                dp[h1 - 2][w1] = -2
                                queue_warp.append([h1 - 2, w1])
                            else:
                                dp[h1 - 2][w1] = -3

            if w1 > 0:
                if dp[h1][w1 - 1] == -1 or dp[h1][w1 - 1] == -2:
                    if m[h1][w1 - 1] == '.':
                        dp[h1][w1 - 1] = now
                        queue.append([h1, w1 - 1])
                    else:
                        dp[h1][w1 - 1] = -3
                if dp[h1][w1 - 1] == -3:
                    fl_left = True
                    if w1 > 1:
                        if dp[h1][w1 - 2] == -1:
                            if m[h1][w1 - 2] == '.':
                                dp[h1][w1 - 2] = -2
                                queue_warp.append([h1, w1 - 2])
                            else:
                                dp[h1][w1 - 2] = -3

            if h1 < h - 1:
                if dp[h1 + 1][w1] == -1 or dp[h1 + 1][w1] == -2:
                    if m[h1 + 1][w1] == '.':
                        dp[h1 + 1][w1] = now
                        queue.append([h1 + 1, w1])
                    else:
                        dp[h1 + 1][w1] = -3
                if dp[h1 + 1][w1] == -3:
                    fl_down = True
                    if h1 < h - 2:
                        if dp[h1 + 2][w1] == -1:
                            if m[h1 + 2][w1] == '.':
                                dp[h1 + 2][w1] = -2
                                queue_warp.append([h1 + 2, w1])
                            else:
                                dp[h1 + 2][w1] = -3

            if w1 < w - 1:
                if dp[h1][w1 + 1] == -1 or dp[h1][w1 + 1] == -2:
                    if m[h1][w1 + 1] == '.':
                        dp[h1][w1 + 1] = now
                        queue.append([h1, w1 + 1])
                    else:
                        dp[h1][w1 + 1] = -3
                if dp[h1][w1 + 1] == -3:
                    fl_right = True
                    if w1 < w - 2:
                        if dp[h1][w1 + 2] == -1:
                            if m[h1][w1 + 2] == '.':
                                dp[h1][w1 + 2] = -2
                                queue_warp.append([h1, w1 + 2])
                            else:
                                dp[h1][w1 + 2] = -3

            if fl_up and fl_left:
                for i in range(max(0, h1 - 2), h1):
                    for j in range(max(0, w1 - 2), w1):
                        if dp[i][j] == -1:
                            if m[i][j] == '.':
                                dp[i][j] = -2
                                queue_warp.append([i, j])
                            else:
                                dp[i][j] = -3

            if fl_left and fl_down:
                for i in range(h1 + 1, min(h, h1 + 3)):
                    for j in range(max(0, w1 - 2), w1):
                        if dp[i][j] == -1:
                            if m[i][j] == '.':
                                dp[i][j] = -2
                                queue_warp.append([i, j])
                            else:
                                dp[i][j] = -3

            if fl_down and fl_right:
                for i in range(h1 + 1, min(h, h1 + 3)):
                    for j in range(w1 + 1, min(w, w1 + 3)):
                        if dp[i][j] == -1:
                            if m[i][j] == '.':
                                dp[i][j] = -2
                                queue_warp.append([i, j])
                            else:
                                dp[i][j] = -3

            if fl_right and fl_up:
                for i in range(max(0, h1 - 2), h1):
                    for j in range(w1 + 1, min(w, w1 + 3)):
                        if dp[i][j] == -1:
                            if m[i][j] == '.':
                                dp[i][j] = -2
                                queue_warp.append([i, j])
                            else:
                                dp[i][j] = -3

            if not queue:
                now += 1
                while queue_warp:
                    h1, w1 = queue_warp.popleft()
                    if dp[h1][w1] == -2:
                        dp[h1][w1] = now
                        queue.append([h1, w1])

            if dp[dh - 1][dw - 1] >= 0:
                return dp[dh - 1][dw - 1]

        return dp[dh - 1][dw - 1]

    h, w = list(map(int, input().split()))
    ch, cw = list(map(int, input().split()))
    dh, dw = list(map(int, input().split()))

    m = [[] for i in range(h)]
    dp = [[-1] * w for i in range(h)]
    dp[ch - 1][cw - 1] = 0

    for i in range(h):
        m[i] = input()

    ans = bfs(ch - 1, cw - 1, dp)

    print(ans)


main()
