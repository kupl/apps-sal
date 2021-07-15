a = [int(input()) for _ in range(5)]
k = int(input())

if max(a) - min(a) > k:
    print(':(')
else:
    print('Yay!')
