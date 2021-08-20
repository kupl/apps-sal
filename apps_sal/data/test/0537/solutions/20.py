l = input()
(n, k) = l.split(' ')
n = int(n)
k = int(k)
winmax = n / 2
nd = winmax / (k + 1)
nd = int(nd)
print(str(nd) + ' ' + str(k * nd) + ' ' + str(n - (k + 1) * nd))
