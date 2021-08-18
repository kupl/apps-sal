
def rint():
    return int(input())


def rints():
    return list(map(int, input().split()))


n = rint()
p = sorted((float(s) for s in input().split()), reverse=True)
pr = 0
inv = 1
for pi in p:
    npr = pr * (1 - pi) + inv * pi
    if npr < pr:
        break
    pr = npr
    inv *= (1 - pi)
print(pr)
