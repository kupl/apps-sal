N = int(input())
strN = str(N)
keta_wa = 0
for i in range(len(strN)):
    keta_wa += int(strN[i])
if N % keta_wa == 0:
    print('Yes')
else:
    print('No')
