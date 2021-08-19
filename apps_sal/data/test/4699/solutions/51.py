(n, k) = [int(x) for x in input().split()]
a = input().split()


def check(p):
    p = list(str(p))
    for i in range(len(p)):
        if p[i] in a:
            return False
    return True


for i in range(n, n * 10000):
    if check(i):
        print(i)
        break
