
def doStuff():
    l = []

    for i in range(4000000):
        l.append((i * i) % 123)

    l.sort()


doStuff()

s = list(map(int, input().split(' ')))[1:]
s.sort()

s = list(map(str, s))


ans = ' '.join(s)
print(ans)
