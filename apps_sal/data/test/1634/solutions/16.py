def readln(): return tuple(map(int, input().split()))


c = readln()
n, m = readln()
a = readln()
b = readln()

va = min(sum([min(c[1], c[0] * _) for _ in a]), c[2])
vb = min(sum([min(c[1], c[0] * _) for _ in b]), c[2])

print(min(va + vb, c[3]))
