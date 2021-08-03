N = int(input())
A = list(map(int, input().split()))
K = max(A)
ls = [0 for i in range(K + 2)]
for i in range(N):
    if A[i] == 0:
        ls[A[i]] += 1
        ls[A[i] + 1] += 1
    else:
        ls[A[i] - 1] += 1
        ls[A[i]] += 1
        ls[A[i] + 1] += 1
print(max(ls))
