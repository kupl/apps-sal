d = (input().split(' '))
n = int(d[0])
sayfa = int(d[1])
i = 0
d = list(map(lambda x: int(x), input().split(' ')))
while sayfa > 0:
    sayfa = sayfa - (86400 - d[i])
    i += 1
print(i)
