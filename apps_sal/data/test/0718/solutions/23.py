3
n = int(input())
c = 1
n += 1
while str(n).find('8') == -1:
    c += 1
    n += 1
print(c)
