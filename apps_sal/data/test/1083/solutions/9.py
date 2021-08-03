n = int(input())

if n % 4 == 0:
    print(0)
    data = []
    for i in range(1, n + 1, 4):
        data.append(str(i) + ' ' + str(i + 3))
elif n % 4 == 3:
    print(0)
    data = []
    for i in range(4, n + 1, 4):
        data.append(str(i) + ' ' + str(i + 3))
    data.append('1 2')
elif n % 4 == 1:
    print(1)
    data = []
    for i in range(2, n + 1, 4):
        data.append(str(i) + ' ' + str(i + 3))
    data.append('1')
else:
    print(1)
    data = []
    for i in range(3, n + 1, 4):
        data.append(str(i) + ' ' + str(i + 3))
    data.append('1')
data = ' '.join(data).split()
print(len(data), ' '.join(data))
