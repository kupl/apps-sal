N = int(input())
N_List = list(map(int,input().split()))[-1::-1] 
for i in range(1,N):
    if N_List[i-1] < N_List[i]:
        if N_List[i-1] + 1 == N_List[i]:
            N_List[i] -= 1
        else:
            print("No")
            break
else:
    print("Yes")
