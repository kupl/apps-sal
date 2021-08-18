n = int(input())
aas = list(map(int, input().split()))
acc = 0
res = 0
r = 0
for i in range(n):
    ok = True
    while r < n:
        s = format(aas[r], '020b')
        acc_s = format(acc, '020b')
        for j in range(20):
            if s[j] == '1':
                if acc_s[j] == '1':
                    ok = False
        if ok:
            acc += aas[r]
            r += 1
        else:
            break
    if r < n:
        res += r - i
    else:
        res += r - i
    acc -= aas[i]
print(res)
