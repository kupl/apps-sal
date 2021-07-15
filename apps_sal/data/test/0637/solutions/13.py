n = int(input())
ln = 0
start = 1
last = -1
check = 1
x = list(map(int, input().split()))
for i in range(n):
    num = x[i]
    if num != last:
        if ln == 0:
            ln = i + 1 - start
        else:
            if i + 1 - start != ln:
                check = 0
        start = i + 1
    last = num
if ln != 0 and n + 1 - start != ln:
    check = 0
if check == 0:
    print('NO')
else:
    print('YES')
