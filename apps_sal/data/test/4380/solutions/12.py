A, B = map(int, input().split())
flg = False
for i in range(1, 4):
    if A * B * i % 2 == 1:
        flg = True
        break
if flg:
    print('Yes')
else:
    print('No')
