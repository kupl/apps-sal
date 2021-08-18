N = int(input())
A = list(map(int, input().split()))


sm = [0]
for i in range(N):
    sm.append(sm[i] + A[i])

ans = 0
for j in range(N):
    ans += A[j] * (sm[N] - sm[j + 1])

print(ans % (10**9 + 7))
