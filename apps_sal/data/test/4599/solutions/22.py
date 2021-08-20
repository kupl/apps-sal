N = int(input())
A = list(map(int, input().split()))
A.sort()
S = 0
T = 0
ans = 0
for i in range(N):
    if N % 2 == 0:
        if i % 2 != 0:
            S += A[i]
        else:
            T += A[i]
        ans = S - T
    else:
        if i % 2 != 0:
            T += A[i]
        else:
            S += A[i]
        ans = S - T
print(ans)
