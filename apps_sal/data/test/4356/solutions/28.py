n, m = list(map(int, input().split()))
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]
for x, a in enumerate(A):
    if x > n - m + 1:
        break
    for i in range(n - m + 1):
        if a[i: i + m] == B[0]:
            for j in range(m):
                if A[x + j][i: i + m] != B[j]:
                    break
            else:
                print("Yes")
                return
print("No")
