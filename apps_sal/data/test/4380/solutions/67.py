(A, B) = map(int, input().split())
flg = True
for i in range(1, 4):
    if A * B * i % 2 == 1:
        flg = False
if flg == False:
    print('Yes')
elif flg == True:
    print('No')
