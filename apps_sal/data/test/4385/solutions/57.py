l = [int(input()) for i in range(5)]
k = int(input())
if max(l) - min(l) <= k:
    print('Yay!')
else:
    print(':(')
