k = list(map(int, input().split()))
for i in range(2**4):
    eat = 0
    noeat = 0
    for j in range(4):
        if (i >> j & 1):
            eat += k[j]
        else:
            noeat += k[j]
    if eat == noeat:
        print("Yes")
        return
print("No")
