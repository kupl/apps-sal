N, M = map(int, input().split())
L_lis = []
R_lis = []
for i in range(M):
    L, R = map(int, input().split())
    L_lis.append(L)
    R_lis.append(R)
new_L, new_R = max(L_lis), min(R_lis)
if new_L <= new_R:
    print(new_R - new_L + 1)
else:
    print(0)
