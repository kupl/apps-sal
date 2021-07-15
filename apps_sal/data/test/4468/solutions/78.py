N,T = map(int,input().split())
N_List = list(map(int,input().split()))

ans = 0
for i in range(1,N):
    ans += (T,N_List[i]-N_List[i-1])[N_List[i]-N_List[i-1]<=T]

ans += T
print(ans)
