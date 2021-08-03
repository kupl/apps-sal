n = int(input())
a = int(n / 7)
check = False
for i in range(a, -1, -1):
    if (n - 7 * i) % 4 == 0:
        check = True
if check:
    print('Yes')
else:
    print('No')
