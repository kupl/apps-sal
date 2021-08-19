# your code goes here

str = input()
L = str.split()
n = int(L[0])
m = int(L[1])

str = input()
L = str.split()
max1 = int(L[0])
min1 = int(L[0])

i = 0

while i < n:
    if max1 < int(L[i]):
        max1 = int(L[i])
    if min1 > int(L[i]):
        min1 = int(L[i])
    i += 1

str = input()
L = str.split()

min = int(L[0])

i = 0

while i < m:
    if min > int(L[i]):
        min = int(L[i])
    i += 1

i = 0

flag = False
if max1 < min:
    i = max1
    while i < min:
        if 2 * min1 <= i:
            print(i)
            flag = True
            i = min + 1
        i += 1

if flag == False:
    print("-1")
