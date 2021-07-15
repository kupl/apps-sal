n, b, p = map(int, input().split())
r1 = 0
r2 = p * n
while n != 1:
    curr = 1
    while curr * 2 <= n:
        curr *= 2
    n -= curr // 2
    r1 += curr * b + curr // 2
print(r1, r2)
