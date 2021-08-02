n = int(input())
a = list(map(int, input().split()))
q = int(input())

d = {}
cnt = sum(a)

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in range(q):
    b, c = map(int, input().split())
    if b in d:
        if c not in d:
            d[c] = 0
        e = d.pop(b)
        d[c] += e
        cnt += (c - b) * e
    print(cnt)
