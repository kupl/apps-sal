n = int(input())
A = list(map(int, ' '.join(input()).split()))
res = 1
for i in range(1, len(A)):
    if A[i] != A[i - 1]:
        res += 1
print(min(res + 2, n))
