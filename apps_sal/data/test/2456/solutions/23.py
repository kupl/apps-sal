import sys
lines = sys.stdin.readlines()
T = int(lines[0].strip())
for t in range(T):
    (n, r) = map(int, lines[t + 1].strip().split(" "))
    mini = min(n - 1, r)
    res = mini * (mini + 1) // 2
    if n - 1 < r:
        res += 1
    print(res)
