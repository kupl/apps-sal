K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

dif = []

for i, a in enumerate(A[:len(A) - 1]):
    dif.append(A[i + 1] - a)

dif.append(K - A[len(A) - 1] + A[0])

print((K - max(dif)))
