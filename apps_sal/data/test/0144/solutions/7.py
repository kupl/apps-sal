def check(a, count):
    ks = 0
    for i in range(len(a)):
        ks += a[i]
        if ks > count:
            return False
        elif ks == count:
            ks = 0

    return True


n = int(input())
a = list(map(int, list(input())))
ss = sum(a)
flag = False
for k in range(2, 1000):
    if ss % k == 0:
        if check(a, ss // k):
            flag = True
            break
if flag:
    print('YES')
else:
    print('NO')
