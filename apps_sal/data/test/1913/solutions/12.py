def f(x):
    s = '1' + '0' * (len(x) - 1)
    if s == x:
        return 1
    elif x == '0':
        return -1
    else:
        return 0


n = int(input())
a = [i for i in input().split()]
count = 0
res = '1'
for i in a:
    if f(i) == 1:
        count += len(i) - 1
    elif f(i) == 0:
        res = i
    else:
        res = '0'
        break
if res == '0':
    print(res)
else:
    print(res + '0' * count)
