N = int(input())
A = list(map(int, input().split()))
A.append(0)
r = 0
ans = 0
su = 0
for l in range(N):
    while (l == r or su + A[r] == su ^ A[r]) and r < N:
        su += A[r]
        r += 1
    ans += r - l
    su -= A[l]
print(ans)
