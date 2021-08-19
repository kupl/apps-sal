n = int(input())
s = input()
a = [0] * 10
for i in range(n):
    a[int(s[i])] = 1
if a[1] + a[2] + a[3] == 0 or a[7] + a[9] + a[0] == 0 or a[1] + a[4] + a[7] + a[0] == 0 or (a[3] + a[6] + a[9] + a[0] == 0):
    print('NO')
else:
    print('YES')
