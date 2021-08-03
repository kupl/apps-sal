N = int(input())
arr = list(map(int, input().split(' ')[:N]))
i = 0
comp = 0
while i < N and arr[i] == arr[0]:
    comp += 1
    i += 1
flag = True
while i < N:
    c2 = 0
    check = arr[i]
    while i < N and arr[i] == check:
        i += 1
        c2 += 1
    if comp != c2:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')
