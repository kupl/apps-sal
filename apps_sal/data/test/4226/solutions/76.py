x, y = map(int, input().split())
flg = False
for i in range(x + 1):
    j = x - i
    if(i * 2 + j * 4 == y):
        flg = True
        break
print('Yes' if flg else 'No')
