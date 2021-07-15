__author__ = 'hamed1soleimani'

ipt = input().split()
s = 0
for i in range(len(ipt)):
    ipt[i] = int(ipt[i])
    s += ipt[i]
if s < 5:
    print(-1)
elif s % 5 == 0:
    print(s // 5)
else:
    print(-1)


