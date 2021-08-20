k = int(input())
ans = 1


def next(n):
    nStr = list(map(int, list(str(n))))
    r = len(nStr) - 1
    while r > 0:
        if nStr[r] <= nStr[r - 1] and (not (nStr[r - 1] == 9 and nStr[r] == 9)):
            break
        r -= 1
    if r == 0 and nStr[0] == 9:
        nStr = [1] + [0] * len(nStr)
    else:
        extra = len(nStr) - 1 - r
        nStr = nStr[:r] + [nStr[r] + 1]
        for _ in range(extra):
            nStr.append(max(0, nStr[-1] - 1))
    return int(''.join(map(str, nStr)))


for i in range(k - 1):
    ans = next(ans)
print(ans)
