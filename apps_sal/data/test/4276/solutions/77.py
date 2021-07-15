n, T = map(int, input().split())
c = [0 for _ in range(n)]
t = [0 for _ in range(n)]
for i in range(n):
    c[i], t[i] = map(int, input().split())

ans = 1001

for i in range(n):
    if t[i] <= T:
        ans = min(ans, c[i])
print(ans if ans != 1001 else "TLE")
