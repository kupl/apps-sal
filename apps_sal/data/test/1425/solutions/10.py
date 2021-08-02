n = int(input())
A = list(map(int, input().split()))
A = sorted(A)
if A[n - 1] >= A[n - 2] + A[n - 3]:
    print("NO")
else:
    used = [0] * n
    print("YES")
    for i in range(n):
        if i % 2 == n % 2:
            print(A[i], end=' ')
            used[i] = 1
    for i in range(n - 1, -1, -1):
        if used[i] == 0:
            print(A[i], end=' ')
