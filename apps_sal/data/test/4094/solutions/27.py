mod = int(input())
a = {}
b = int(0)
flag = int(0)
ans = int(0)
for i in range(mod):
    b = b * 10 + 7
    b = b % mod
    if b == 0:
        flag = 1
        ans = int(i) + 1
        break
    else:
        pass
if flag == 1:
    print(ans)
else:
    print('-1')
