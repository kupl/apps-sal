n, s = input().split()
n = int(n)
ans = 0
AT, GC = 0, 0
cnt = {}
cnt[(0, 0)] = 1
for i in s:

    if i == "A":
        AT += 1
    elif i == "T":
        AT -= 1
    elif i == "G":
        GC += 1
    elif i == "C":
        GC -= 1
    if (AT, GC) in cnt:
        ans += cnt[(AT, GC)]
        cnt[(AT, GC)] += 1
    else:
        cnt[(AT, GC)] = 1
    #print(cnt, ans)
print(ans)
