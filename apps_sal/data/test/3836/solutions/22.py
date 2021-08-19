n = int(input())
lis10 = []
lis01 = []
lis00 = []
inf = c11 = c10 = c01 = c = c00 = 0
for i in range(n):
    a, b = list(map(str, input().split()))
    if a == '11':
        inf += int(b)
        c11 += 1
    elif a == '10':
        c10 += 1
        lis10.append(int(b))
    elif a == '01':
        c01 += 1
        lis01.append(int(b))
    else:
        c00 += 1
        lis00.append(int(b))
lis10.sort(reverse=True)
lis01.sort(reverse=True)
c = min(c01, c10)
for i in range(c):
    inf += (lis10[i] + lis01[i])
lis00 += lis10[c:c10] + lis01[c:c01]
lis00.sort(reverse=True)
# if len(lis00)<c11:
#    print(inf)
# else:
for i in range(min(c11, len(lis00))):
    inf += lis00[i]
print(inf)
