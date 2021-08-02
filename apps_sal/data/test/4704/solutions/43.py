N = int(input())
A = [int(a) for a in input().split(" ")]

sA = []
for i in range(len(A)):
    if i == 0:
        sA.append(A[0])
    else:
        sA.append(sA[i - 1] + A[i])

s = sum(A)
dA = [abs(2 * sA[j] - s) for j in range(len(sA) - 1)]

print(min(dA))
