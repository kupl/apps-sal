(n, m, q) = [int(i) for i in input().split()]
s = list(input())
t = list(input())
lt = len(t)
ls = len(s)
start = []
for i in range(ls - lt + 1):
    j = i
    count = 0
    while s[j] == t[count]:
        j += 1
        count += 1
        if count >= lt:
            break
    if count == lt:
        start.append(i + 1)
start += [n + 1]
for i in range(q):
    (l, r) = [int(j) for j in input().split()]
    r -= lt - 1
    if l > r:
        print(0)
        continue
    f = False
    for j in range(len(start)):
        if f == False and start[j] >= l:
            f = True
            begin = j
        if f and start[j] > r:
            end = j
            break
    print(end - begin)
