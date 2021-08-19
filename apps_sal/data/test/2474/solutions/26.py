N = int(input())
C = list(map(int, input().split()))
MOD = 1000000007
B = [0 for _ in range(N + 1)]
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
'\nD = [0 for _ in range(N)]#累積和\nD[0] = C[0]\nfor i in range(1,N):\n  D[i] = D[i-1] + C[i]\nprint(C)\n\n  \nans = 0\nfor j in range(1,N+1):\n  ans += D[j-1] * B[j-1]  \n  print(D[j-1] * B[j-1]  \n  \n'
