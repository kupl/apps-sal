n = int(input())
a = [0] * (n // 2 + 1)
k = [0] * (n // 2 + 1)
j = 0
df = False
for i in range(n):
    str = input().split()
    if str[0] == 'add':
        a[j] += 1
    if str[0] == 'for':
        j += 1
        k[j] = int(str[1])
    if str[0] == 'end':
        j -= 1
        a[j] += a[j + 1] * k[j + 1]
        a[j + 1] = 0
    if a[j] >= 4294967296:
        df = True

        break
if df == True:
    print('OVERFLOW!!!')
else:
    print(a[0])
