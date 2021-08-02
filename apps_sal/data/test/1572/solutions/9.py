3


def readln(): return tuple(map(int, input().split()))


n, = readln()
a = readln()
l = [0] * n
l[0] = 1
for _ in range(1, n):
    if _ > 1 and a[_] == a[_ - 1] + a[_ - 2]:
        l[_] = l[_ - 1] + 1
    else:
        l[_] = 2
print(max(l))
