N = int(input())
N_List = list(map(int,input().split()))
cnt = 0
while len(N_List) != 0:
    N_List = [i//2 for i in N_List if i % 2 == 0].copy()
    cnt += len(N_List)
print(cnt)
