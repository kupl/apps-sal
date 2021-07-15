n = str(input())
a = []
for i in n:
    a.append(int(i))
b = sum(a)
if int(n) % b == 0:
    print('Yes')
else:
    print('No')
