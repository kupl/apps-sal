w = str(input())
data1 = []
for i in range(len(w)):
    data1.append(w[i])
data2 = []
for i in range(len(w)):
    if not w[i] in data2:
        data2.append(w[i])
error = 0
for x in data2:
    if data1.count(x) % 2 != 0:
        error += 1
        break
if error == 0:
    print('Yes')
else:
    print('No')
