N = int(input())
M = N // 2
A = [int(a) - 1 for a in input().split()]
B = [0] * (N)
ANS = []
for i in range(N):
    B[A[i]] = i


def calc(i):
    j = B[i]
    if j == i:
        return 0
    if abs(j - i) >= M:
        ANS.append(str(i + 1) + " " + str(j + 1))
    elif i < M and j < M:
        ANS.append(str(i + 1) + " " + str(N))
        ANS.append(str(j + 1) + " " + str(N))
        ANS.append(str(i + 1) + " " + str(N))
    elif i >= M and j >= M:
        ANS.append(str(1) + " " + str(i + 1))
        ANS.append(str(1) + " " + str(j + 1))
        ANS.append(str(1) + " " + str(i + 1))
    elif i < M:
        ANS.append(str(i + 1) + " " + str(N))
        ANS.append(str(1) + " " + str(N))
        ANS.append(str(1) + " " + str(j + 1))
        ANS.append(str(1) + " " + str(N))
        ANS.append(str(i + 1) + " " + str(N))
    else:
        ANS.append(str(j + 1) + " " + str(N))
        ANS.append(str(1) + " " + str(N))
        ANS.append(str(1) + " " + str(i + 1))
        ANS.append(str(1) + " " + str(N))
        ANS.append(str(j + 1) + " " + str(N))

    m = A[i]
    A[i], A[B[i]] = i, A[i]
    B[m] = B[i]
    B[i] = i


for i in range(N):
    calc(i)
print(len(ANS))

print("\n".join(ANS))
