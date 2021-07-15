n, a, b = list(map(int, input().split()))
ans = 0

for i in range(1,n+1):
    mod = 0
    div = i
    while div > 0:
        mod += (div % 10)
        div //= 10
    if mod >= a and mod <= b:
        ans += i

print(ans)

