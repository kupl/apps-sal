n = int(input())

s = "{0:b}".format(n)
l = len(s)

for k in range(int(l / 2), -1, -1):
    b = ''.join(['1'] * (k + 1) + ['0'] * k)
    n2 = int(b, 2)
    if n2 <= n and n % n2 == 0:
        print(n2)
        break
