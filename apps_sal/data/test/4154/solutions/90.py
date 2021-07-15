N, M = map(int, input().split())

L_list = []
R_list = []

for i in range(M):
    A, B = map(int, input().split())
    L_list.append(A)
    R_list.append(B)

if max(L_list) > min(R_list):
    print(0)
else:
    print(min(R_list) - max(L_list) + 1)
