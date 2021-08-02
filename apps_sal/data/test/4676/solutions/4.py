a = input()
b = input()
li = []
if len(a) == len(b):
    for i in range(len(a)):
        li.append(a[i] + b[i])
else:
    for i in range(len(b)):
        li.append(a[i] + b[i])
    li.append(a[-1])
print(''.join(li))
