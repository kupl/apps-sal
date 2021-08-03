N = int(input())
P_list = list(map(int, input().split()))

now = 1
pre = -1
ans = []
for i in range(N):
    if P_list[i] == now:
        for j in range(i - 1, pre, -1):
            P_list[j], P_list[j + 1] = P_list[j + 1], P_list[j]
            ans.append(j + 1)
        now = i + 1
        pre = i - 1

if P_list == sorted(P_list) and len(ans) == N - 1:
    print(*ans, sep='\n')
else:
    print(-1)
