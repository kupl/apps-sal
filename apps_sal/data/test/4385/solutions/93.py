a, b, c, d, e, k = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
if k >= max(a, b, c, d, e) - min(a, b, c, d, e):
    print('Yay!')
else:
    print(':(')
