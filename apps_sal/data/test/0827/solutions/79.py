n = int(input())
s = input()
flag = True
if n == 1:
    if s == '0':
        print(pow(10, 10))
    elif s == '1':
        print(pow(10, 10) * 2)
elif n == 2:
    if s in ['11', '10']:
        print(pow(10, 10))
    elif s == '01':
        print(pow(10, 10) - 1)
    else:
        print(0)
else:
    flag = True
    f = n // 3
    r = n % 3
    for i in range(0, n, 3):
        if i == 0:
            ans = s[0:3]
            if ans not in ['110', '101', '011']:
                flag = False
                break
        elif i < 3 * f:
            tmp = s[i:i + 3]
            if tmp != ans:
                flag = False
                break
        else:
            tmp = s[i:n]
            if tmp != ans[0:n - i]:
                flag = False
                break
    if not flag:
        print(0)
    elif ans == '110':
        if r == 0:
            print(pow(10, 10) - f + 1)
        else:
            print(pow(10, 10) - f)
    elif ans == '101':
        print(pow(10, 10) - f)
    elif ans == '011':
        if r < 2:
            print(pow(10, 10) - f)
        else:
            print(pow(10, 10) - f - 1)
