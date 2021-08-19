(n, a, b) = (int(s) for s in input().split())
if a * b < n:
    print(-1)
elif b % 2:
    for i in range(a):
        print(*[j if j <= n else 0 for j in range(i * b + 1, (i + 1) * b + 1)])
else:
    for i in range(a):
        if i % 2:
            print(*[j if j <= n else 0 for j in range(i * b + 1, (i + 1) * b + 1)])
        else:
            print(*[j if j <= n else 0 for j in range(i * b + 1, (i + 1) * b + 1)][::-1])
