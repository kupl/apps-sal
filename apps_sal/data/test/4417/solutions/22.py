q = int(input())
for _ in range(q):
    (n, k) = list(map(int, input().split()))
    u = list(map(int, input().split()))
    m1 = min(u)
    m2 = max(u)
    if m2 - m1 > 2 * k:
        print(-1)
        continue
    print(m1 + k)
