N = int(input())
N_List = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans += N_List[i]-1
print(ans)
