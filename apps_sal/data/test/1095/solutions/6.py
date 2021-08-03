# coding:utf-8

n, _ = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
m, _ = map(int, input().strip().split())
b = list(map(int, input().strip().split()))


def solve(T):
    nonlocal a, b
    d = dict()
    for i in b:
        pos = i % T
        if pos in d:
            d[pos] += 1
        else:
            d[pos] = 1
    for i in a:
        pos = (i + T / 2) % T
        if pos in d:
            d[pos] += 1
        else:
            d[pos] = 1
    return max(d.values())


T = 2
ans = 0
while True:
    ans = max(ans, solve(T))
    T *= 2
    if T > 1e9:
        break

if len(set(a) and set(b)) > 0:
    ans = max(ans, 2)
print(ans)
