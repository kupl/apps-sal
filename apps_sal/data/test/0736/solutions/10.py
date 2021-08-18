
(n, m) = list(map(int, input().split()))

ok = False
for step2 in range(n // 2, -1, -1):
    step = step2 + (n - 2 * step2)
    if step % m == 0:
        print(step)
        ok = True
        break

if not ok:
    print(-1)
