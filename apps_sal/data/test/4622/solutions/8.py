num = int(input())
table = list(map(int, input().split()))
count = 0
list.sort(table)
if num == 2:
        if table[0] == table[1]:
            count += 1
else:
    for i in range(1, num-1):
        if num == 2:
            if table[0] == table[1]:
                count += 1
        elif table[i] == table[i+1] or table[i-1] == table[i]:
            count += 1
        else:
            continue
if count == 0:
    print('YES')
else:
    print('NO')
