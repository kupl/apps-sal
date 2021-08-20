n = int(input())
x = n
n = str(n)
f = 0
for i in range(len(n)):
    y = int(n[i])
    f += y
if x % f == 0:
    print('Yes')
else:
    print('No')
