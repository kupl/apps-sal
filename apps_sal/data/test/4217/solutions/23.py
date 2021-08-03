N, M = list(map(int, input().split()))
con = 0
like = 0
List = []
for i in range(1, N + 1):
    L = list(map(int, input().split()))
    for a in range(L[0]):
        b = L[a + 1]
        List.append(b)
for j in range(1, M + 1):
    con = 0
    for k in List:
        if k == j:
            con += 1
    if con == N:
        like += 1
print(like)
