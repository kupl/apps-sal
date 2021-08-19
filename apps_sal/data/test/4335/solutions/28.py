b = int(input())
a = input()
c = []
for i in range(b):
    c.append(a[i])
if b == 1:
    print('No')
elif c[:int(b / 2)] == c[int(b / 2):]:
    print('Yes')
else:
    print('No')
