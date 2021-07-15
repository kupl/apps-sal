n, s = list(map(int, input().split()))
a = [int(el) for el in input().split()]
b = [int(el) for el in input().split()]
s -= 1
if (a[0] == 0) or (a[s] == 0 and b[s] == 0):
    print('NO')
else:
    if a[s] == 1:
        print('YES')
    else:
        ss = 'NO'
        for i in range(s, n):
            if a[i] + b[i] == 2:
                ss = 'YES'
        print(ss)

