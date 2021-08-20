N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    if A[i] >= B[i]:
        ans += B[i]
        A[i] -= B[i]
    else:
        temp = B[i] - A[i]
        ans += A[i]
        if A[i + 1] >= temp:
            ans += temp
            A[i + 1] -= temp
        else:
            ans += A[i + 1]
            A[i + 1] = 0
print(ans)
