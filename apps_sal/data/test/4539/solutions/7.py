a = input()
y = []
for i in range(len(a)):
    y.append(int(a[i]))
if int(a) % sum(y) == 0:
    print('Yes')
else:
    print('No')
