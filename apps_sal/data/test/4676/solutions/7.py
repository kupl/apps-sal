a = list(input())
b = list(input())
f = False
x = []
if len(a) > len(b):
    b.append(0)
    f = True
for i in range(len(a)):
    x.append(a[i])
    x.append(b[i])
if f:
    x.pop()
print(''.join(x))
