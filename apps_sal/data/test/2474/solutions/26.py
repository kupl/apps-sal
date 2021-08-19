N = int(input())
C = list(map(int, input().split()))
MOD = 1_000_000_007

B = [0 for _ in range(N + 1)]  # 2べきmod
B[0] = 1
for i in range(1, N + 1):
    B[i] = B[i - 1] * 2
    B[i] %= MOD

C.sort()

ans = 0
for n in range(1, N + 1):
    ans += C[n - 1] * ((N - n) * B[N - n - 1] + B[N - n]) * B[n - 1]
    ans %= MOD

ans *= B[N]
ans %= MOD

print(ans)

"""
D = [0 for _ in range(N)]#累積和
D[0] = C[0]
for i in range(1,N):
  D[i] = D[i-1] + C[i]
print(C)

  
ans = 0
for j in range(1,N+1):
  ans += D[j-1] * B[j-1]  
  print(D[j-1] * B[j-1]  
  
"""
