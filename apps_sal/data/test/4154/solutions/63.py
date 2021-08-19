N, M = map(int, input().split())
L = [0] * M
R = [0] * M

for i in range(M):
    L[i], R[i] = map(int, input().split())

L_SORT = sorted(L)
R_SORT = sorted(R)

# print(L_SORT)
# print(R_SORT)

L_MAX = L_SORT[M - 1]
R_MIN = R_SORT[0]

# print(L_MAX)
# print(R_MIN)


if (R_MIN - L_MAX) < 0:
    print(0)
else:
    print(R_MIN - L_MAX + 1)
