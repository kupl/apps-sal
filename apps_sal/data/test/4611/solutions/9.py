n=int(input())
n_list=[[0,0,0]]
for i in range(n):
    n_list.append(list(map(int,input().split())))

for t in range(n):
    dt=n_list[t+1][0]-n_list[t][0]
    dist=abs(n_list[t+1][1]-n_list[t][1])+abs(n_list[t+1][2]-n_list[t][2])

    if(dist>dt):
        can='No'
        break
    xy=n_list
    if(dist%2 != dt%2):
        can='No'
        break
    can='Yes'
print(can)
