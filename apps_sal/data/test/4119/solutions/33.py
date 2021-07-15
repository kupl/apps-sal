N,M  = map(int,input().split())
N_List = sorted(list(map(int,input().split())))
N_Diff =[]
for i in range(1,M):
    N_Diff.append(N_List[i]-N_List[i-1])
if N >= M:
    ans = 0
elif M == 1:
    ans = sum(N_Diff)
else:
    ans = sum(sorted(N_Diff)[:M-N])
print(ans)
