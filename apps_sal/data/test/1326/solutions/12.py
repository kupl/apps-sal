N = int(input())
ans = 0
for i in range(1,N+1):
    k = N // i
    ans += i * k * (k+1) // 2
print(ans)
