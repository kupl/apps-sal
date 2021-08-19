n = int(input())
a = [int(x) for x in input().split()]
flag = False
for i in range(n):
    if a[a[a[i] - 1] - 1] - 1 == i:
        flag = True
        break
print('YES' if flag else 'NO')
