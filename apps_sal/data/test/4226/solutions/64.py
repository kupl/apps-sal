(x, y) = list(map(int, input().split()))
flag = 0
for i in range(x + 1):
    if i * 2 + (x - i) * 4 == y:
        print('Yes')
        flag = 1
        break
if flag == 0:
    print('No')
