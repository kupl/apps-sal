n = int(input())

arr = []
for i in range(4*n + 1):
    str_ = input()
    x, y = str_.split()
    arr.append((int(x), int(y)))

arr.sort()

n1 = 4*n+1

i = 1
while arr[i][0] == arr[i-1][0]:
    i += 1

if i == 1:
    print(str(arr[0][0]) + ' ' + str(arr[0][1]))
    return
low_x = arr[0][0]

i = n1-2
while arr[i][0] == arr[i+1][0]:
    i -= 1
if i == n1-2:
    print(str(arr[n1-1][0]) + ' ' + str(arr[n1-1][1]))
    return
high_x = arr[n1-1][0]


for i in range(n1):
    arr[i] = (arr[i][1], arr[i][0])

arr.sort()
i = 1
while arr[i][0] == arr[i-1][0]:
    i += 1
if i == 1:
    print(str(arr[0][1]) + ' ' + str(arr[0][0]))
    return
low_y = arr[0][0]

i = n1-2
while arr[i][0] == arr[i+1][0]:
    i -= 1
if i == n1-2:
    print(str(arr[n1-1][1]) + ' ' + str(arr[n1-1][0]))
    return
high_y = arr[n1-1][0]

for i in range(n1):
    arr[i] = (arr[i][1], arr[i][0])

for i in range(n1):
    if not (arr[i][0] == low_x or arr[i][0] == high_x or arr[i][1] == low_y or arr[i][1] == high_y):
        print(str(arr[i][0]) + ' ' + str(arr[i][1]))
        return


