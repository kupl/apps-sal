n = int(input())
walk = list(map(int, input().split()))
MAXN = 1000000000


def solve1():
    for i in range(n - 1):
        if abs(walk[i + 1] - walk[i]) != 1:
            return False
    print("YES")
    print(MAXN, 1)
    return True


def solve2():
    colum = -1
    for i in range(n - 1):
        diff = abs(walk[i + 1] - walk[i])
        if diff != 1:
            if colum == -1:
                colum = diff
            elif colum != diff:
                return False
    if colum <= 0:
        return False
    for i in range(n - 1):
        if abs(walk[i + 1] - walk[i]) == 1 and ((walk[i + 1] - 1) // colum != (walk[i] - 1) // colum):
            return False
    print("YES")
    print(MAXN, colum)
    return True


if solve1():
    pass
elif solve2():
    pass
else:
    print("NO")
