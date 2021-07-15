# B
n = int(input())
ps = list(map(int, input().split()))
count=0
c_ps=sorted(ps)
for i in range(n):
    if ps[i]!=c_ps[i]:
        count+=1

if count in [0,2]:
    print('YES')
else:
    print('NO')
