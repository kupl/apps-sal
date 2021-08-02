N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())
sortedA = sorted(A)
if sortedA[N - 1] == sortedA[N - 2]:
    for _ in range(N):
        print(sortedA[N - 1])
else:
    for i in range(N):
        if A[i] != sortedA[N - 1]:
            print(sortedA[N - 1])
        else:
            print(sortedA[N - 2])
