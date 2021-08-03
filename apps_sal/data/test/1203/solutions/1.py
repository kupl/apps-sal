H, L = list(map(int, input().split(' ')))
out = (L**2 - H**2) / (2 * H * 1.0)
print('{0:.13f}'.format(out))
