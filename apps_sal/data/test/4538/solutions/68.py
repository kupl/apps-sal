import math

n, d = list(map(int, input().split()))

a = 0
ans = 0

n_l = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    n_l.append(tmp)

for i in n_l:
    for j in i:
        a += j ** 2
    b = math.sqrt(a)
    if b <= d:
        ans += 1
    a = 0

print(ans)
