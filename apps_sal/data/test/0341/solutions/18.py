N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = input()

T_split = [[] for i in range(K)]
for i in range(N):
    T_split[i%K].append(T[i])
#print(T_split)

ans = 0
flag = 0

for i in range(len(T_split)):
    for j in range(len(T_split[i])):
        if flag == 1:
            flag = 0
            continue
        if T_split[i][j] == 'r':
            point = P
        elif T_split[i][j] == 's':
            point = R
        elif T_split[i][j] == 'p':
            point = S
        ans += point
        if j != len(T_split[i]) - 1:
            if T_split[i][j] == T_split[i][j+1]:
                flag = 1
print(ans)

