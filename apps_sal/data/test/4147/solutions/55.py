from itertools import product
(n, a, b, c) = list(map(int, input().split()))
l = [int(input()) for _ in range(n)]
ans = 1001001001
for x in product(list(range(4)), repeat=n):
    s = [0] * 4
    t = -3
    for i in range(n):
        t += x[i] < 3
        s[x[i]] += l[i]
    s.pop()
    if 0 in s:
        continue
    ans = min(ans, t * 10 + abs(s[0] - a) + abs(s[1] - b) + abs(s[2] - c))
print(ans)
