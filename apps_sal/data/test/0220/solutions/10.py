(s, x) = list(map(int, input().split()))
jj = 1 if s >= x and (s - x) / 2 == (s - x) // 2 else 0
xx = bin(x)[2:]
aa = bin((s - x) // 2)[2:]
if len(xx) < len(aa):
    xx = (len(aa) - len(xx)) * '0' + xx
else:
    aa = (len(xx) - len(aa)) * '0' + aa
for i in range(len(xx)):
    if xx[i] == '0':
        continue
    elif xx[i] == '1':
        if aa[i] == '0':
            jj *= 2
        else:
            jj = 0
if (s - x) // 2 == 0 and jj >= 2:
    jj -= 2
print(jj)
