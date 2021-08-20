n = int(input())
l = list(map(int, input().split()))
l.sort()
cost = sum([i - 1 for i in l])
c = 2
con = True
while con:
    tmp = 0
    cc = 1
    for i in range(n):
        tmp += abs(l[i] - cc)
        if cost < tmp:
            con = False
            break
        cc *= c
    if con:
        cost = tmp
    c += 1
print(cost)
