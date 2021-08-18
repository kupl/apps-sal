import sys

N, C = map(int, sys.stdin.readline().split())

times = [[set() for _ in range(10**5 + 5)], [set() for _ in range(10**5 + 5)]]
max_t = 0
for _ in range(N):
    s, t, c = map(int, sys.stdin.readline().split())
    times[0][s - 1].add(c)
    times[0][s].add(c)
    times[1][t].add(c)
    max_t = max(max_t, t)

ans = 0
recording = set()
for i in range(max_t + 5):
    recording -= times[1][i]
    recording |= times[0][i]
    ans = max(ans, len(recording))

print(ans)
