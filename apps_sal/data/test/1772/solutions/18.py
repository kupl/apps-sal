cntn = 0
cntc = 0
n = int(input())
s = input().split(' ')
for i in s:
    if int(i) % 2 == 0:
        cntn = cntn + 1
    else:
        cntc = cntc + 1
k = min(cntc, cntn)
if cntc > cntn:
    k = max(k, cntn + (cntc - cntn) // 3)
print(k)
