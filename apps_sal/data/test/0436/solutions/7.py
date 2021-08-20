n = int(input())
A = list(map(int, input().split()))
ans = [1]
Sum = A[0]
for i in range(1, n):
    if A[0] >= 2 * A[i]:
        Sum += A[i]
        ans.append(i + 1)
if 2 * Sum > sum(A):
    print(len(ans))
    for a in ans:
        print(a, end=' ')
else:
    print(0)
