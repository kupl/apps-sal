N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]

AB.sort(key=lambda x:x[1])
total=0
for i in range(N):
    total+=AB[i][0]
    if total<=AB[i][1]:
        continue
    else:
        print('No')
        return

print('Yes')
