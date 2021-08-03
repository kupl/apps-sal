n, k = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
d = 0
ans = 0
for i in range(n):
    sum += b[i]
    if sum >= k:
        while sum >= k:
            ans += n - i
            sum -= b[d]
            d += 1
print(ans)
