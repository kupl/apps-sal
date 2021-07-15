n, k = map(int, input().split())

while k > 0:
    k -= 1
    if n % 10 == 0:
        n = n // 10
    else:
        n -= 1

print(n)
