def new_print(arr):
    print(''.join(arr))


n = int(input())
str = input()
l0 = str.count('0')
l1 = str.count('1')
l2 = str.count('2')
str = list(str)
real = n // 3
cur = 0
while l0 < real:
    if str[cur] == '1' and l1 > real:
        l1 -= 1
        l0 += 1
        str[cur] = '0'
    if str[cur] == '2' and l2 > real:
        l2 -= 1
        l0 += 1
        str[cur] = '0'
    cur += 1
cur = 0
while l1 < real and cur < len(str) and (l2 > real):
    if str[cur] == '2':
        l2 -= 1
        l1 += 1
        str[cur] = '1'
    cur += 1
cur = len(str) - 1
while l2 < real and cur >= 0:
    if str[cur] == '1' and l1 > real:
        l2 += 1
        l1 -= 1
        str[cur] = '2'
    if str[cur] == '0' and l0 > real:
        l2 += 1
        l0 -= 1
        str[cur] = '2'
    cur -= 1
cur = len(str) - 1
while l1 < real and cur >= 0:
    if str[cur] == '0' and l0 > real:
        l1 += 1
        l0 -= 1
        str[cur] = '1'
    cur -= 1
new_print(str)
