N = int(input())
N_List = list(map(int, input().split()))
ans = 1
maxN = N_List[0]
for i in range(1, N):
    if N_List[i] >= maxN:
        ans += 1
        maxN = N_List[i]
print(ans)
