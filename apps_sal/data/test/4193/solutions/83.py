ls = []
for i in range(3):
    ls += list(map(int,input().split()))
N = int(input())
lsb = [int(input()) for i in range(N)]
for i in range(N):
    if lsb[i] in ls:
        ls[ls.index(lsb[i])] = '#'
ans = 'No'
for i in range(3):  
    if ls[0+i] == '#' and ls[3+i] == '#' and ls[6+i] == '#':
        ans = 'Yes'
for i in range(3):  
    if ls[3*i] == '#' and ls[3*i+1] == '#' and ls[3*i+2] == '#':
        ans = 'Yes'
if ls[0] == '#' and ls[4] == '#' and ls[8] == '#':
        ans = 'Yes'
if ls[2] == '#' and ls[4] == '#' and ls[6] == '#':
        ans = 'Yes'
print(ans)
