N,M = map(int,input().split())
N_List = []
O_List = []

for i in range(M):
    a,b = map(int,input().split())
    if a == 1:
        N_List.append(b)
    if b == 1:
        N_List.append(a)
    if a == N:
        O_List.append(b)
    if b == N:
        O_List.append(a)

print(("IMPOSSIBLE","POSSIBLE")[len(set(N_List) & set(O_List)) > 0])
