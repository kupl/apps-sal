n = int(input())
a = sorted(map(int, input().split()))
r1 = sum(abs(a[i] - 2 * i - 1) for i in range(n // 2))
r2 = sum(abs(a[i] - 2 * i - 2) for i in range(n // 2))
print(min(r1, r2))

