n = int(input())
q = list(map(int, input().split()))
r = 0
p = [0] * n
for i in range(len(q)):
    r += (i + 1) * q[i]
if (r + (n + 1) * n // 2) % n == 0:
    p[n - 1] = (r + (n + 1) * n // 2) // n
    s = sum(q)
    for i in range(n - 1):
        p[i] = p[n - 1] - s
        s -= q[i]
    if sorted(p) == list(range(1, n + 1)):
        print(*p)
    else:
        print(-1)
else:
    print(-1)

