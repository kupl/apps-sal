t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m1 = min(a)
    m2 = max(a)
    if m2 - m1 < k:
        print(m1 + k)
    elif m2 - m1 > 2 * k:
        print(-1)
    else:
        print(m1 + k)
