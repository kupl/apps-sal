A, B = list(map(int, input().split()))

N = 100

A -= 1
B -= 1

S = []
for i in range(N // 2):
    S.append(list("." * N))
for i in range(50):
    S.append(list("#" * N))

flag = 0
for i in range(1, N // 2, 2):
    for j in range(1, N, 2):
        if B == 0:
            flag = 1
            break
        else:
            S[i][j] = "#"
            B -= 1
    if flag:
        break

flag = 0
for i in range(N // 2 + 1, N, 2):
    for j in range(1, N, 2):
        if A == 0:
            flag = 1
            break
        else:
            S[i][j] = "."
            A -= 1
    if flag:
        break

print((N, N))
for i in range(N):
    print(("".join(S[i])))
