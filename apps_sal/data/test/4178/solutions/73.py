N = int(input())
A = list(map(int, input().split()))

ans = 'Yes'
for i in range(N - 1, 0, -1):
    if A[i] < A[i - 1]:
        A[i - 1] -= 1
    if A[i] < A[i - 1]:
        ans = 'No'
        break

print(ans)
