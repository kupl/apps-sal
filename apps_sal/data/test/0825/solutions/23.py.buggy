from collections import defaultdict

N = int(input())

if N == 1:
    print(0)
    return

p = defaultdict(int)

while N % 2 == 0:
    p[2] += 1
    N //= 2
f = 3
while f * f <= N:
    if N % f == 0:
        p[f] += 1
        N //= f
    else:
        f += 2
if N != 1:
    p[N] += 1

ans = 0

for v in p.values():
    n = 1
    i = 1
    while n <= v:
        ans += 1
        i += 1
        n += i

print(ans)
