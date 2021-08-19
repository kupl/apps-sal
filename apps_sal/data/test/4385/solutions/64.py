l = [int(input()) for i in range(6)]
k = l[-1]
sub = l[-2] - l[0]
if sub <= k:
    print('Yay!')
else:
    print(':(')
