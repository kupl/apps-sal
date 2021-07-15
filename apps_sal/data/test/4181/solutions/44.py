N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
ans = 0
for i in range(N):
    p = A[i] + A[i+1]
    if(p - B[i] >= 0):
        ans += B[i]
        if(A[i] - B[i] < 0):
            A[i+1] = p - B[i]
    else:
        ans += p
        A[i+1] = 0
print(ans)
