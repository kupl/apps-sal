from math import gcd
N = int(input())
A = list(map(int, input().split()))

L = [A[0]]
R = [A[-1]]

for i in range(1, N):
    L.append(gcd(L[-1], A[i]))
    R.append(gcd(R[-1], A[-1 - i]))
R = R[::-1]

ans = 1
for j in range(N):
    if j == 0:
        tmp = R[1]
    elif j == N - 1:
        tmp = L[N - 2]
    else:
        tmp = gcd(L[j - 1], R[j + 1])
    ans = max(ans, tmp)

print(ans)
