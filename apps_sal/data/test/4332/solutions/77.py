n = int(input())
nl = list(str(n))
l = len(nl)
sn = 0
for i in range(l):
    sn += int(nl[i])
if n % sn == 0:
    print('Yes')
else:
    print('No')
