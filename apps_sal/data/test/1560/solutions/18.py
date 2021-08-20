n = int(input())
s = input()
srr = 0
srb = 0
sbr = 0
sbb = 0
ansr = 0
ansb = 0
ans = 0
for i in range(n):
    if s[i] == 'r':
        if (i + 1) % 2 == 0:
            srr += 1
        else:
            sbr += 1
    elif (i + 1) % 2 == 0:
        sbb += 1
    else:
        srb += 1
if srr + srb < sbr + sbb:
    (ansr, ansb) = (srr, srb)
else:
    (ansr, ansb) = (sbr, sbb)
x = min(ansr, ansb)
ans = x + (max(ansr, ansb) - x)
print(ans)
