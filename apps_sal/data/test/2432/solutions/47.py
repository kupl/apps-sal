n = int(input())
b = ''
n = "{0:b}".format(n)
if len(n) != 7:
    n = '0' * (7 - len(n)) + n

b += n[0] + n[1] + n[6] + n[4] + n[3] + n[5] + n[2]

print(int(b, 2))
