n = int(input())
A = input().split()
A = [0] + [int(ai) for ai in A]
valid_k = []
for k in range(1, n + 1):
    X = []
    isvalid = True
    for i in range(1, n + 1):
        if i <= k:
            X.append(A[i] - A[i - 1])
        elif X[(i - 1) % k] != A[i] - A[i - 1]:
            isvalid = False
            break
    if isvalid:
        valid_k.append(k)
print(len(valid_k))
print(' '.join([str(k) for k in valid_k]))
