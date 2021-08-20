a = input()
b = []
c = 0
for i in range(len(a)):
    b.append(a[i])
b.sort()
for i in range(len(a) - 1):
    if b[i] == b[i + 1]:
        c = c + 1
if c == 0:
    print('yes')
else:
    print('no')
