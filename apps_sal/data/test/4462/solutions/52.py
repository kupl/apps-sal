n = int(input())
a = list(map(int, input().split()))
c_ki = 0
c_4 = 0
c_2 = 0
for i in range(n):
    if a[i] % 2 == 1:
        c_ki += 1
    elif a[i] % 4 == 0:
        c_4 += 1
    else:
        c_2 += 1
if c_ki <= c_4:
    print('Yes')
elif c_ki - 1 == c_4 and c_2 == 0:
    print('Yes')
else:
    print('No')
