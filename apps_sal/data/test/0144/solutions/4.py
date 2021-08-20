n = int(input())
a = input()
ans = 0
needs = 0
for i in range(n):
    needs += int(a[i])
    currs = 0
    for j in range(i + 1, n):
        currs += int(a[j])
        if currs > needs:
            break
        elif currs == needs:
            if j == n - 1:
                ans = 1
                break
            elif a[j + 1] != '0':
                currs = 0
if ans:
    print('YES')
else:
    print('NO')
