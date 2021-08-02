N = int(input())
A = list(map(int, input().split()))
A.reverse()
ans = "Yes"
for i in range(N - 1):
    if A[i] >= A[i + 1]:
        continue
    elif A[i] == A[i + 1] - 1:
        A[i + 1] = A[i]
    else:
        ans = "No"
print(ans)
