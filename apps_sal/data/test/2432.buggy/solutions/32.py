a = int(input())
abin = format(a, '06b')
l = [abin[0], abin[5], abin[3], abin[2], abin[4], abin[1]]
x = ''.join(l)
print(int(x, 2))
