n = int(input().strip())
ais = list(map(int, input().strip().split()))


def ceil(a, b):
    return -(-a // b)


bis = [ceil(ai - i, n) for (i, ai) in enumerate(ais)]
bmin = min(bis)
ibmin = bis.index(bmin)
print(ibmin + 1)
