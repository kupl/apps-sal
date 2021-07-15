n = input()
n1 = len(n)
su = 0
for i in range(n1):
    su += int(n[i])
if int(n)%su==0:
    print('Yes')
else:
    print('No')
