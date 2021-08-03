

N, M = map(int, input().split())
H = list(map(int, input().split()))
A = [0] * M
B = [0] * M
Lists = [[] for _ in range(N)]
for i in range(M):
    A[i], B[i] = map(lambda x: int(x) - 1, input().split())
    Lists[A[i]].append(B[i])
    Lists[B[i]].append(A[i])

# print(Lists)
ans = 0
for i in range(N):
    Heighest = 0
    # print(Lists[i])
    #print("H[i]:", H[i])
    for j in range(len(Lists[i])):
        #print("H[List[i][j]]:", H[Lists[i][j]])
        Heighest = max(Heighest, H[Lists[i][j]])
    # print(Heighest)
    # print(H[i])
    if Heighest < H[i]:
        #print("Heighest = ", Heighest)
        ans += 1

print(ans)
