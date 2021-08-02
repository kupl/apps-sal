a, b = input().split()
a = list(a)
b = int(b)


def findMax(a, f, dist):
    m = f
    for i in range(f + 1, min(f + dist + 1, len(a))):
        if a[i] > a[m]:
            m = i
    return m


pos = 0
while b > 0 and pos < len(a):
    m = findMax(a, pos, b)
    #print('we found:', m)
    a.insert(pos, a.pop(m))
    #print('new a', a)
    b -= m - pos
    #print('new b', b)
    pos += 1

print(''.join(a))
