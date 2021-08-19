all = {}
n = int(input())
ans = True
for i in range(n):
    x_k = input().split()
    x = int(x_k[0])
    k = int(x_k[1])
    if k not in all:
        all[k] = -1
    if all[k] >= x:
        pass
    elif all[k] + 1 != x:
        ans = False
        break
    else:
        all[k] = x
if ans:
    print('YES')
else:
    print('NO')
