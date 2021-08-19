n = int(input())
ccnt = {}
sn = {}
for i in range(1, n + 1):
    s = input()
    res = eval(s)
    res = str(format(res, '.6f'))
    if res in ccnt:
        ccnt[res] += 1
    else:
        ccnt[res] = 1
    sn[i] = res
for i in range(1, n + 1):
    print(str(ccnt[sn[i]]) + ' ', end='')
print()
