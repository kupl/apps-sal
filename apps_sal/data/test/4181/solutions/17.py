N = int(input())
M_List = list(map(int, input().split()))
N_List = list(map(int, input().split()))
ans = 0
for i in range(N):
    if N_List[i] >= M_List[i]:
        ans += M_List[i]
        ans += (M_List[i + 1], N_List[i] - M_List[i])[N_List[i] - M_List[i] <= M_List[i + 1]]
        M_List[i + 1] = max(0, M_List[i + 1] - (N_List[i] - M_List[i]))
    else:
        ans += N_List[i]
print(ans)
