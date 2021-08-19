# map(int,input().split())
n = int(input())
a = list(map(int, input().split()))
ans = 0
flag = 0
for i in range(1, n):
    if a[i] == 2:
        if a[i - 1] == 3:
            print('Infinite')
            flag = 1
            break
        else:
            ans += 3
            if i > 1 and a[i - 2] == 3:
                ans -= 1
    elif a[i] == 1:
        if a[i - 1] == 2:
            ans += 3
        else:
            ans += 4
    else:
        if a[i - 1] == 2:
            print('Infinite')
            flag = 1
            break
        else:
            ans += 4
if flag == 0:
    print('Finite')
    print(ans)
