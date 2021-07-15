n, b, p = list(map(int, input().split()))

ans1 = 0
ans2 = p * n
while n != 1:
    k = 1
    while k * 2 <= n:
        k *= 2
    ans1 += k // 2 + b * k
    n -= k // 2

print(ans1, ans2)

