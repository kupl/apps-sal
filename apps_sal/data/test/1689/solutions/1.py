n = int(input())
arr = []
for i in range(n):
    arr.append(input())

suc = 0
for i in range(n):
    x = arr[i]
    if(x[0:2]=='OO'):
        suc = 1
        arr[i] = '++'+x[2:]
        break
    if(x[3:5]=='OO'):
        suc = 1
        arr[i] = x[:3]+'++'
        break
if(suc):
    print('YES')
    for x in arr:
        print(x)
else:
    print('NO')
