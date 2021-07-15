from bisect import *

a = sorted(input())
b = input()

if len(a) < len(b):
    print(''.join(reversed(a)))
    return

res = ''
lower = False
for i in range(len(b)):
    # print('i = ', i)
    # print('a = ', a)
    for j in range(len(a) - 1, -1, -1):
        bb = b[i + 1 :]
        aa = a[:j] + a[j + 1:]
        if a[j] < b[i] or a[j] == b[i] and ''.join(aa) <= bb:
            res += a[j]
            a = aa
            break
    if res[-1] < b[i]:
        break

print(res + ''.join(reversed(a)))
