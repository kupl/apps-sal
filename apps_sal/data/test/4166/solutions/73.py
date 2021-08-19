(N, M) = list(map(int, input().split()))
sc_list = [list(map(int, input().split())) for i in range(M)]
order_list = [0] * N
ans = 0
for i in range(M):
    if sc_list[i][0] == 1 and sc_list[i][1] == 0 and (N > 1):
        ans = -1
        break
    for j in range(i + 1, M):
        if sc_list[i][0] == sc_list[j][0] and sc_list[i][1] != sc_list[j][1]:
            ans = -1
            break
if ans == 0:
    if N > 1:
        order_list[0] = 1
    for (i, j) in sc_list:
        order_list[i - 1] = j
    for i in range(N):
        ans += order_list[i] * 10 ** (N - i - 1)
print(ans)
