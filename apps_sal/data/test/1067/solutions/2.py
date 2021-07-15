n = int(input())
a = list(map(int, input().split()))
num = 0
mi = 0
zero = 0
for i in range(n):
    if a[i] == 0:
        num += 1
        zero += 1
    elif a[i] > 0:
        num += a[i] - 1
    else:
        num += abs(a[i]) - 1
        mi += 1

if zero > 0:
    print(num)
else:
    if mi % 2 != 0:
        print(num + 2)
    else:
        print(num)
