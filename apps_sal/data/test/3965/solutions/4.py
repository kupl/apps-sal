n = int(input())
a = list(map(int, input().split()))
b = {'a', 'e', 'o', 'u', 'i', 'y'}
fl = 1
for i in range(n):
    s = input()
    k = 0
    for j in s:
        if j in b:
            k += 1
    if k != a[i]:
        fl = 0
        break
if fl:
    print('YES')
else:
    print('NO')
