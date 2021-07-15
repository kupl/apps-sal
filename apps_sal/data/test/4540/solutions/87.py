N = int(input())
N_List = [0] +list(map(int,input().split())) + [0]
N_Diff_List = []

for i in range(N+1):
    N_Diff_List.append(abs(N_List[i+1]-N_List[i]))

sumans = sum(N_Diff_List)
for i in range(N):
    ans = sumans -(N_Diff_List[i] + N_Diff_List[i+1])
    ans += abs(N_List[i+2]-N_List[i])
    print(ans)

