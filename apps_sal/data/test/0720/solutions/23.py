import sys
def inpl(): return list(map(int, sys.stdin.readline().split()))


N = int(input())

ans = 1
a, b = 0, 0

for _ in range(N):
    c, d = inpl()
    candi = []
    if a == b:
        ans -= 1
    if a <= d <= c:
        candi.append(d)
    if a <= b <= c:
        candi.append(b)
    if b <= a <= d:
        candi.append(a)
    if b <= c <= d:
        candi.append(c)
    if len(candi) >= 2:
        maxi = max(candi)
        mini = min(candi)
        ans += maxi - mini + 1
    a, b = c, d
print(ans)
