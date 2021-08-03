from math import factorial


def comb(n, r):
    if n - r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


n, a, b = map(int, input().split())
v = list(map(int, input().split()))
mod = 10**9 + 7
v.sort(reverse=True)
x = v[a - 1]
cnt = 0
s = 0
for i in range(n):
    if x == v[i]:
        cnt += 1
    if x < v[i]:
        s = i + 1
ans = 0
print(sum(v[:a]) / a)
if v[0] == v[a - 1]:
    for i in range(a, min(cnt + 1, b + 1)):
        ans += comb(cnt, i)
    print(ans)
else:
    ans = comb(cnt, a - s)
    print(ans)
