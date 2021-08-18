from sys import stdin
def rd(l): return tuple(map(int, l.split()))


n, a, b = rd(input())
b = min(n, b)
s = list(map(rd, stdin.readlines()))


def f(x): return max(0, x[0] - x[1])
def g(x): return (x[0] << a) - x[1]


ans = sum(x[1] for x in s)
mid = 0
if b:
    s.sort(key=f, reverse=True)
    t = sum(f(x) for x in s[:b])
    for i in range(b):
        mid = max(mid, t - f(s[i]) + g(s[i]))
    for i in range(b, n):
        mid = max(mid, t - f(s[b - 1]) + g(s[i]))
    ans += mid
print(ans)
