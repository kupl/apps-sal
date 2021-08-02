arr = [[] for i in range(9)]
for i in range(3):
    q = list(input().split())
    arr[0] += q[0]
    arr[1] += q[1]
    arr[2] += q[2]
q = input()
for i in range(3):
    q = list(input().split())
    arr[3] += q[0]
    arr[4] += q[1]
    arr[5] += q[2]
q = input()
for i in range(3):
    q = list(input().split())
    arr[6] += q[0]
    arr[7] += q[1]
    arr[8] += q[2]
x, y = list(map(int, input().split()))
x %= 3
y %= 3
if x == 1:
    if y == 1:
        pos = 0
    elif y == 2:
        pos = 1
    else:
        pos = 2
elif x == 2:
    if y == 1:
        pos = 3
    elif y == 2:
        pos = 4
    else:
        pos = 5
else:
    if y == 1:
        pos = 6
    elif y == 2:
        pos = 7
    else:
        pos = 8
if '.' in arr[pos]:
    for i in range(9):
        if arr[pos][i] == '.':
            arr[pos][i] = '!'
else:
    for i in range(9):
        for j in range(9):
            if arr[i][j] == '.':
                arr[i][j] = '!'

ans = []
for i in range(3):
    q = ''
    for j in range(3):
        for l in range(3):
            q += arr[j][i * 3 + l]
        q += ' '
    ans.append(q)
ans.append(' ')
for i in range(3):
    q = ''
    for j in range(3):
        for l in range(3):
            q += arr[3 + j][i * 3 + l]
        q += ' '
    ans.append(q)
ans.append(' ')
for i in range(3):
    q = ''
    for j in range(3):
        for l in range(3):
            q += arr[6 + j][i * 3 + l]
        q += ' '
    ans.append(q)
for i in range(11):
    print(ans[i])
