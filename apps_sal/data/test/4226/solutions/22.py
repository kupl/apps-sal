x, y = map(int, input().split())
flag = False
for i in range(x+1):
    if 2 * i + 4 * (x-i) == y:
        flag = True
        break
if flag:
    print('Yes')
else:
    print('No')
