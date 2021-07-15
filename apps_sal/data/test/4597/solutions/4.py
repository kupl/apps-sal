N = int(input())
ans = 1
for i in range(1, N+1):
    ans = ans * i % (10**9+7)
print(ans % (10**9+7))
