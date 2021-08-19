def inpmap():
    return list(map(int, input().split()))


n = int(input())
arr = list(inpmap())
dc = {}
for i in range(n):
    x = arr[i]
    while x in dc:
        del dc[x]
        x *= 2
    dc[x] = i
print(len(dc))
print(*dc)
