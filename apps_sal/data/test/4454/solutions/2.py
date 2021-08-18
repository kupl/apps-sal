
def rint():
    return int(input())


def rints():
    return list(map(int, input().split()))


q = rint()
for _ in range(q):
    n = rint()
    a = rints()
    print((sum(a) + n - 1) // n)
