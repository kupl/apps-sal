def do():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    i = 0
    totalNeed = 0
    while(1):
        if (i + 1 >= n):
            break
        curSum = a[i] + a[i + 1]
        need = k - curSum
        totalNeed += max(0, need)
        if (need > 0):
            a[i + 1] += need
        i += 1
    print(totalNeed)
    return a


rs = do()
tobeprinted = ""
for r in rs:
    tobeprinted += (str(r) + " ")
print(tobeprinted[:-1])
