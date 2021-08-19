from collections import Counter
(n, a, b) = [int(_) for _ in input().split()]
(s, s1) = (Counter(), Counter())
ans = 0
for i in range(n):
    (x, vx, vy) = [int(_) for _ in input().split()]
    tmp = vy - a * vx
    ans += s[tmp] - s1[vx, vy]
    s[tmp] += 1
    s1[vx, vy] += 1
print(ans * 2)
