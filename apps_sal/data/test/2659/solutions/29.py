k = int(input())
ans = []
for i in range(1, 10):
    ans.append(str(i))

for i in range(1, 10):
    ans.append(str(i) + '9')

for i in range(1, 10):
    ans.append(str(i) + '99')

for i in range(10):
    ans.append('1' + str(i) + '99')
for i in range(2, 10):
    ans.append(str(i) + '999')

for i in range(1, 3):
    for j in range(10):
        ans.append(str(i) + str(j) + '999')
for i in range(3, 10):
    ans.append(str(i) + '9999')

for i in range(1, 4):
    for j in range(10):
        ans.append(str(i) + str(j) + '9999')
for i in range(4, 10):
    ans.append(str(i) + '99999')

for i in range(1, 5):
    for j in range(10):
        ans.append(str(i) + str(j) + '99999')
for i in range(5, 10):
    ans.append(str(i) + '999999')

for i in range(1, 6):
    for j in range(10):
        ans.append(str(i) + str(j) + '999999')
for i in range(6, 10):
    ans.append(str(i) + '9999999')

for i in range(1, 7):
    for j in range(10):
        ans.append(str(i) + str(j) + '9999999')
for i in range(7, 10):
    ans.append(str(i) + '99999999')

for i in range(1, 8):
    for j in range(10):
        ans.append(str(i) + str(j) + '99999999')
for i in range(8, 10):
    ans.append(str(i) + '999999999')

for i in range(1, 9):
    for j in range(10):
        ans.append(str(i) + str(j) + '999999999')
for i in range(9, 10):
    ans.append(str(i) + '9999999999')

for i in range(1, 10):
    for j in range(10):
        ans.append(str(i) + str(j) + '9999999999')
for i in range(10, 10):
    ans.append(str(i) + '99999999999')

for i in range(1, 10):
    for j in range(10):
        ans.append(str(i) + str(j) + '99999999999')
for i in range(10, 10):
    ans.append(str(i) + '999999999999')

for i in range(1, 10):
    for j in range(10):
        ans.append(str(i) + str(j) + '999999999999')
for i in range(10, 10):
    ans.append(str(i) + '9999999999999')

for i in range(10):
    ans.append('10' + str(i) + '999999999999')
for i in range(1, 10):
    ans.append('1' + str(i) + '9999999999999')
for i in range(2, 10):
    for j in range(10):
        ans.append(str(i) + str(j) + '9999999999999')

for val in ans[:k]:
    print(val)
