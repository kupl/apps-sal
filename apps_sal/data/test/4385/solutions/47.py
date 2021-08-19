antena = [int(input()) for i in range(5)]
k = int(input())
if antena[-1] - antena[0] <= k:
    print('Yay!')
else:
    print(':(')
