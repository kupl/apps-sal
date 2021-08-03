def I(): return int(input())


def sign(x): return -1 if(x < 0) else 1


def LI(): return [sign(int(x)) for x in input().split()]
def c(x): return x * (x - 1) // 2


n = I()
a = LI()
for i in range(1, len(a)):
    a[i] *= a[i - 1]

p = 0
i = 0
for x in a:
    if(x == -1):
        i += 1
    else:
        p += 1

print(c(n) + n - (c(p) + c(i) + p), c(p) + c(i) + p)
