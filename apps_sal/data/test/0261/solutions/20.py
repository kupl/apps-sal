n = int(input())
s = list(input())
F = False
for k in range(1, (n + 3) // 4 + 1):
    for i in range(n - 3):
        flag = True
        for j in range(5):
            if i + j * k >= n or s[i + j * k] == '.':
                flag = False
        if flag:
            F = True
            break
    if F:
        break
if F:
    print('yes')
else:
    print('no')
