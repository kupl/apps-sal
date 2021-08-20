n = int(input())
A = list(map(int, input().split()))
S = set(A)
D = {}
for i in A:
    if i in list(D.keys()):
        D[i] += 1
    else:
        D[i] = 1
p = sorted(list(D.items()), key=lambda x: x[1])
max_number = p[-1][0]
first_index = A.index(max_number)
print(len(A) - p[-1][1])
for i in range(first_index - 1, -1, -1):
    if A[i] < max_number:
        x = 1
    else:
        x = 2
    print(x, i + 1, i + 2)
for i in range(first_index + 1, n):
    if A[i] == max_number:
        continue
    if A[i] < max_number:
        x = 1
    else:
        x = 2
    print(x, i + 1, i)
