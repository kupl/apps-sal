n = int(input())
A = [int(i) for i in input().split()]
A.sort()
if A[0] > 1:
    A[0] -= 1
ans = 1
for i in range(1, n):
    if A[i] == A[i - 1]:
        A[i] += 1
        ans += 1
    elif A[i] > A[i - 1] + 1:
        A[i] -= 1
        ans += 1
    elif A[i] > A[i - 1]:
        ans += 1
    else:
        A[i] = A[i - 1]
print(ans)
