N = int(input())
A = list(map(int, input().split()))
lst = []
for i in range(N):
    lst.append([i + 1, A[i]])
lst.sort(key=lambda x: x[1])
for j in lst:
    print(j[0], end=' ')
