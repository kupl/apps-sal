x = [int(input()) for i in range(5)]
k = int(input())
if x[4] - x[0] <= k:
    print('Yay!')
else:
    print(':(')
