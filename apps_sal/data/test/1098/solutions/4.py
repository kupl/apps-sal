n = int(input())
a = []

for i in range(n):
    str = input()
    h = int(str[0:2]) * 60
    m = int(str[3:5])
    a.append(h + m)

a.sort()

mx = 0

for i in range(n - 1):
    if mx < ((-a[i] + a[i + 1]) - 1):
        mx = ((-a[i] + a[i + 1]) - 1)
if mx < (1440 + a[0] - a[n - 1] - 1):
    mx = 1440 + a[0] - a[n - 1] - 1

if (mx // 60) < 10:
    print('0',end='')
    
print(mx // 60,end='')

print(':',end='')

if (mx % 60) < 10:
    print('0',end='')

print(mx % 60)

