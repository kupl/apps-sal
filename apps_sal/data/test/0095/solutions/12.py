n = int(input())
ar = input().split()
cur = 0
count = 0
bo = False
for i in range(n):
    if int(ar[i]) > cur and count == 0:
        cur = int(ar[i])
    elif int(ar[i]) == cur and count <= 1:
        count = 1
    elif int(ar[i]) < cur and count <= 1:
        count = 2
        cur = int(ar[i])
    elif int(ar[i]) < cur and count == 2:
        cur = int(ar[i])
    else:
        bo = True
        break
if bo:
    print('NO')
else:
    print('YES')

