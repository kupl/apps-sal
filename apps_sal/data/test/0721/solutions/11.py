3

def readln(): return tuple(map(int, input().split()))

n, d = readln()
a = sorted(readln())
m, = readln()
if m <= n:
    print(sum(a[:m]))
else:
    print(sum(a) - (m - n) * d)

