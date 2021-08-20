N = int(input())
A = list(map(int, input().split()))
A.sort()
d = []
for i in range(N - 1):
    if A[i] == A[i + 1]:
        d.append(A[i])
print(N - len(d) if len(d) % 2 == 0 else N - len(d) - 1)
