n = int(input())
s = input()
a = [ord(c) for c in s]
for i in range(0, n):
    if a[i] > 96:
        a[i] = a[i] - 32
counter = 0
for i in range(65, 91):
    for j in range(0, n):
        if a[j] == i:
            counter = counter + 1
            break
if counter == 26:
    print('YES')
else:
    print('NO')
