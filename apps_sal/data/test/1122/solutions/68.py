N, M = list(map(int, input().split()))

n = 2*M+1
# Mが奇数の場合
if M%2==1:
    for i in range(1, M//2+1):
        print(('{} {}'.format(i,M+1-i)))
    for i in range(1, (M+1)//2+1):
        print(('{} {}'.format(M+i,2*M+2-i)))
# Mが偶数の場合
else:
    for i in range(1, M//2+1):
        print(('{} {}'.format(i,M+2-i)))
    for i in range(1, M//2+1):
        print(('{} {}'.format(M+i+1,2*M+2-i)))
    

