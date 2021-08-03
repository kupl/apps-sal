n = int(input())
a = 0
b = 0
flag = True
t = set(list('qwertyuioplkjhgfdsazxcvbnm'))
for i in range(n):
    op, w = list(map(str, input().split()))
    w = set(list(w))
    if op == '!':
        t &= w
        a += 1
        if flag:
            b += 1
    elif op == '.':
        t = t.difference(w)
    else:
        t = t.difference(w)
        if i != n - 1:
            a += 1
            if flag:
                b += 1
    if len(t) == 1:
        flag = False
print(a - b)
