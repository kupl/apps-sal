# ABC127 B

r, D, x = map(int, input().split())
A = []
for i in range(11):
    if i == 0:
        A.append(x)
    else:
        A.append(r * (A[i - 1]) - D)

for j in range(10):
    print(A[j + 1])
