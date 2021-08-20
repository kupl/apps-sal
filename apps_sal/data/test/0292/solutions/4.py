def summ(x):
    ret = 1
    acc = 1
    while acc <= x:
        ret += acc
        acc *= 2
    return ret


(h, n) = list(map(int, input().split()))
ans = 1
lvl = 0
cur = 'L'
amnt = 2 ** h
while 1:
    if lvl == h:
        break
    if cur == 'L':
        if n <= amnt // 2:
            amnt //= 2
            cur = 'R'
            ans += 1
            lvl += 1
        else:
            amnt //= 2
            n -= amnt
            cur = 'L'
            ans += summ(amnt)
            lvl += 1
    elif n <= amnt // 2:
        amnt //= 2
        cur = 'R'
        ans += summ(amnt)
        lvl += 1
    else:
        amnt //= 2
        n -= amnt
        cur = 'L'
        ans += 1
        lvl += 1
print(ans - 1)
