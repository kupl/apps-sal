def feven(pieces, n):
    res = 0
    for i in range(len(pieces)):
        res += abs(pieces[i] - 2 * (1 + i))
    return res
def fodd(pieces, n):
    res = 0
    for i in range(len(pieces)):
        res += abs(pieces[i] - (2 * (1 + i) - 1))
    return res


n = int(input())

pieces = list(map(int, input().split()))

pieces = sorted(pieces)

ans1 = feven(pieces, n)

ans2 = fodd(pieces, n)

print(min(ans1, ans2))
