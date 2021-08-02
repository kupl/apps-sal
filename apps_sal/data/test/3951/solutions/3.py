def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
l = list(map(int, input().split()))
m = {}
ans = []
for x in l:
    m[x] = m.get(x, 0) + 1
for x in sorted(m.keys())[::-1]:
    while m[x]:
        for y in ans:
            m[gcd(x, y)] -= 2
        ans += [x]
        m[x] -= 1
print(' '.join(map(str, ans)))
