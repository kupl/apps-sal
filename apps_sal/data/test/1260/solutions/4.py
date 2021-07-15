n = int(input())

a = list(map(int,input().split()))

ct = 0
mn = 1000000000000000000
pos = 0
is_all_zero = True

for i in range(n):
    x = a[i]
    if x < 0:
        ct += 1
        if mn > abs(x):
            mn = abs(x)
            pos = i



if ct%2 == 1:
    a[pos] = 0

for x in a:
    if x != 0:
        is_all_zero = False
        

if is_all_zero:
    for i in range(n-1):
        print(1,i+1,i+2)
    return


pre = 0
pre0 = 0

for i in range(n):
    if a[i] == 0:
        if pre0:
            print(1,pre0,i+1)
        pre0 = i+1
    else:
        if pre == 0:
            pre = i+1
        else:
            print(1,pre,i+1)
            pre = i+1

if pre0:
    print(2,pre0)
