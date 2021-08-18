import sys
k = int(sys.stdin.readline().split()[1])
t = list(map(lambda s: int(s), sys.stdin.readline().split()))
t.sort()


def find(x, a, b):
    while True:
        if a == b:
            if x == t[a]:
                return a
            else:
                return None
        m = a + (b - a) // 2
        if x > t[m]:
            a = m + 1
        else:
            b = m


u = [True for i in t]
s = 0
for i in range(len(t)):
    if u[i]:
        s += 1
        u[i] = False
        j = find(t[i] * k, 0, len(t) - 1)
        if j is not None:
            u[j] = False
print(s)
