from collections import defaultdict
n = int(input())

d = defaultdict(int)

i = 2
while i * i <= n:
    while n % i == 0:
        d[i] += 1
        n /= i
    i += 1
if n != 1:
    d[n] += 1

ans = 0
for v in list(d.values()):
    # x * (x + 1) // 2 <= vとなる最大のx
    x = 0
    while (x + 1) * (x + 2) // 2 <= v:
        x += 1
    ans += x
print(ans)
