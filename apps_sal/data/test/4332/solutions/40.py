s = input()
n = int(s)
m = list(s)
l = [int(i) for i in m]
su = sum(l)
if n % su == 0:
    print('Yes')
else:
    print('No')
