n = int(input())
A = list(map(int, input().split()))
I = []
for i in range(n):
    for j in range(i + 1, n):
        if A[i] > A[j]:
            I.append([A[i], i + 1, j + 1])
I.sort()
I.sort(key=lambda x: x[2], reverse=True)
print(len(I))
if len(I) > 0:
    for i in I:
        j = i[1:]
        print(*j)
