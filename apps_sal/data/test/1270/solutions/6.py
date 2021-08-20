n = int(input())
l = []
while n >= 4:
    n -= 2
    l.append(2)
l.append(n)
l = list(map(str, l))
print(len(l))
print(' '.join(l))
