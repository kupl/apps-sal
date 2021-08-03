n = int(input())
a = list(map(int, input().split()))
k = []
for i in range(len(a)):
    k.append((a[i], i + 1))
k.sort()
k = k[::-1]
curdate = 0
curpos = 0
while curpos < len(k):
    res = []
    res.append(k[curpos][0])
    for j in range(k[curpos][1] - curdate - 1):
        print()
    curdate = k[curpos][1]
    while curpos + 1 < len(k) and k[curpos + 1][1] <= curdate:
        curpos += 1
        res.append(k[curpos][0])
    curpos += 1
    print(*res)
