n = int(input())
a = list(map(int, input().split()))
flg = 0
for i in a:
    if i % 2 == 0:
        if i % 3 != 0 and i % 5 != 0:
            flg = 1
if flg:
    print('DENIED')
else:
    print('APPROVED')
