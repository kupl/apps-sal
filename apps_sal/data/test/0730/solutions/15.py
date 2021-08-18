a = []
a.append('+------------------------+')
a.append('|
a.append('|
a.append('|
a.append('|
a.append('+------------------------+')
a=list(map(list, a))
curr=[0, 0]
n=int(input())
while n > 0:
    if a[curr[0]][curr[1]] == '
        a[curr[0]][curr[1]]='O'
        n -= 1
    curr[0] += 1
    if curr[0] >= 6:
        curr[0]=0
        curr[1] += 1
for i in range(5):
    for j in a[i][:-1]:
        print(j, end='')
    print(a[i][-1])
for j in a[5]:
    print(j, end='')
