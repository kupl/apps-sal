n = int(input())
n = str(n)
s = 0
for i in n:
    s += int(i)
if int(n) % s == 0:
    print('Yes')
else:
    print('No')
