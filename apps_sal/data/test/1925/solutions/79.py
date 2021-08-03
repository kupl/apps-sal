a, b, n = list(map(int, input().split()))

if b > n:
    x = n

else:
    x = b - 1

ans = int(a * x / b)
print(ans)
