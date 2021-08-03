a = int(input())
b = input()
ans = [0] * 10
for x in b:
    if x == 'L':
        uk = 0
        while ans[uk] == 1:
            uk += 1
        ans[uk] = 1
    elif x == 'R':
        uk = 9
        while ans[uk] == 1:
            uk -= 1
        ans[uk] = 1
    else:
        ans[int(x)] = 0
for x in ans:
    print(x, end='')
