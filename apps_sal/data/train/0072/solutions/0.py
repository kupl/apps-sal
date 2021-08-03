t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if len(set(a)) > k:
        print(-1)
        continue
    l = list(set(a))
    l.extend([1] * (k - len(l)))

    print(n * k)
    for _ in range(n):
        print(*l, end=" ")
    print()
