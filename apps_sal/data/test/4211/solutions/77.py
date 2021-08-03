N = int(input())
B = list(map(int, input().split()))

A = []
A.append(B[0])
for i in range(N - 2):
    if B[i] < B[i + 1]:
        A.append(B[i])
    else:
        A.append(B[i + 1])
A.append(B[N - 2])

print(sum(A))
