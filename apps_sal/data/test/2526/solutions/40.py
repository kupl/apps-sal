x, y, a, b, c = list(map(int, input().split()))

pA = list(map(lambda x: (int(x), "a"), input().split()))
pB = list(map(lambda x: (int(x), "b"), input().split()))
pC = list(map(lambda x: (int(x), "c"), input().split()))

apples = sorted(pA + pB + pC)

cntA = 0
cntB = 0
cntC = 0
cnt = 0

while cntA + cntB + cntC < x + y:
    val, col = apples.pop()

    if col == "a" and cntA < x:
        cntA += 1
        cnt += val
    elif col == "b" and cntB < y:
        cntB += 1
        cnt += val
    elif col == "c":
        cntC += 1
        cnt += val

print(cnt)
