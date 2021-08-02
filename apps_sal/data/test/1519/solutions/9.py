import sys

n, l, a = list(map(int, input().split()))
c = 0
ans = 0
for line in sys.stdin.readlines():
    t, m = list(map(int, line.split()))
    ans += (t - c) // a
    c = t + m
ans += (l - c) // a
print(ans)
