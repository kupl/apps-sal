n = input()
s = 0
n = str(n)
for i in n:
    s += int(i)
if int(n) % s == 0:
    print('Yes')
else:
    print('No')
