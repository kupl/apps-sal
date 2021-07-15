from math import comb
mod = 10 ** 9 + 7
n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
print(sum(v[:a]) / a)
if v[0] != v[a - 1]:
    cur = v[a - 1]
    cnt = 0
    for i in range(n):
        if cur == v[i]:
            cnt += 1
    cnt2 = 0
    for i in range(a):
        if cur == v[i]:
            cnt2 += 1
    print(comb(cnt, cnt2))
else:
    cur = v[a - 1]
    cnt = 0
    for i in range(n):
        if cur == v[i]:
            cnt += 1
    ans = 0
    for i in range(a, b + 1):
        ans += comb(cnt, i)
    print(ans)
