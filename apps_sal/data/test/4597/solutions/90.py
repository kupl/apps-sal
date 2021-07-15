N = int(input())
ans = 1
mod = pow(10, 9)+7
for i in range(1, N+1):
    ans = (ans*i) % mod
print(ans)

