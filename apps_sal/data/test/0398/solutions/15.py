n = int(input())
a = [int(s) for s in input().split()]
a.sort()
flag = False
for i in range(len(a) - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')
