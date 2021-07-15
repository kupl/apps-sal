m, n = list(map(int, input().split()))
D = []
kok = {i for i in range(1, n + 1)}
for i in range(m):
    A = list(map(int, input().split()))
    D.append(set(A[1:]))
for i in range(m):
    for j in range(i + 1, m):
        if D[i].intersection(D[j]) == set():
            print('impossible')
            return
print('possible')

