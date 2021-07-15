N = int(input())

work = [[] for i in range(N)]

for i in range(N):
    a,b = map(int,input().split())
    work[i] = [b,a]

work.sort()
total = 0
for i in range(N):
    total += work[i][1]
    if total > work[i][0]:
        print('No')
        return
print('Yes')
