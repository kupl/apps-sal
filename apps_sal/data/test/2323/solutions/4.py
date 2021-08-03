n = int(input())
answer = []
summa = {}
summa[0] = 0


def bin(p):
    left = 0
    right = lena
    while right - left > 1:
        mid = (left + right) // 2
        if res[mid] <= p:
            left = mid
        else:
            right = mid
    return left + 1


uku = list(set([int(x) for x in input().split()]))
uku.sort()
res = []
for i in range(1, len(uku)):
    res.append(uku[i] - uku[i - 1])
q = int(input())
res.append(10**100)
res.sort()
counter = 0
i = 1
for item in res:
    counter += item
    summa[i] = counter
    i += 1
lena = len(res)
for i in range(q):
    l, r = [int(x) for x in input().split()]
    s = r - l + 1
    counter = 0
    if s < res[0]:
        bina = 0
    else:
        bina = bin(s)
    counter = summa[bina] + s * (lena - bina)

    answer.append(counter)
print(*answer)
