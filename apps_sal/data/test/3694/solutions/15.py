n = int(input())
u = list(map(int, input().split()))
u.sort()
ans = 0
k = 1
ok = False
for i in range(1, n):
    if u[i] == u[i - 1]:
        k += 1
        if k == 3:
            print('cslnb')
            return
        if k == 2:
            if ok or u[i] == 0 or u[i] - u[i - 2] == 1:
                print('cslnb')
                return
            ok = True
    else:
        k = 1
for i in range(n):
    ans += u[i] - i
if ans % 2 == 0:
    print('cslnb')
else:
    print('sjfnb')

