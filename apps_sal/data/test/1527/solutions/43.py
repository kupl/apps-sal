import queue
(h, w) = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            seen = [[0 for _ in range(w)] for _ in range(h)]
            length = [[0 for _ in range(w)] for _ in range(h)]
            q = queue.Queue()
            q.put([i, j])
            seen[i][j] = 1
            while not q.empty():
                (ci, cj) = q.get()
                for (ni, nj) in [[ci - 1, cj], [ci + 1, cj], [ci, cj - 1], [ci, cj + 1]]:
                    if 0 <= ni < h and 0 <= nj < w and (s[ni][nj] == '.') and (seen[ni][nj] == 0):
                        q.put([ni, nj])
                        length[ni][nj] = length[ci][cj] + 1
                        seen[ni][nj] = 1
            ans = max(ans, length[ci][cj])
print(ans)
