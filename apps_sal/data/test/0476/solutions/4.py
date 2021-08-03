x = str(input())
i = 0
while i <= (len(x) - 1):
    if x[i] == '1':
        if x[i:i + 2] == '14':
            if x[i:i + 3] == '144':
                i += 3
            else:
                i += 2
        else:
            i += 1
    else:
        print('NO')
        break
else:
    print('YES')
