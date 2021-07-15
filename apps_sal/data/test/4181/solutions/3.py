
N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
pool = 0
target = 0
for i in range(len(A)):
    if i == len(A)-1:
        if pool >= A[i]:
            ans += A[i]
        else:
            ans += pool
        break

    if pool >= A[i]:
        ans += A[i]
        target = 0
    else:
        ans += pool
        target = A[i] - pool
    ans += min(target,B[i])
    pool = max(0,B[i] - target)


print(ans)
