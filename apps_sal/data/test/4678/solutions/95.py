N = int(input())
A = list(map(int,input().split()))
maximum = A[0]
ans = 0

for i in range(N):
    if maximum >= A[i]:
        ans += (maximum - A[i])
    else:
        maximum = max(maximum, A[i])

print(ans)
