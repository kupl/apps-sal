x = [int(input()) for _ in range(5)]
k = int(input())
M = max(x)
m = min(x)
if M - m > k:
    print(':(')
else:
    print('Yay!')
