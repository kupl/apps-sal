n = str(input())
s = len(n)
h = 0
for i in range(s):
    keta = int(n[i])
    h += keta
if h % 9 == 0:
    print('Yes')
else:
    print('No')
