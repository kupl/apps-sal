n = int(input())
l = [int(i) for i in input()]
d = []
for i in range(n):
    q = [int(o) for o in input().split()]
    d.append(q)

on = l.count(1)
ans = on

for t in range(1, 130):
    # print(t-1, l, ans)
    for i in range(n):
        if t >= d[i][1] and (t-d[i][1]) % d[i][0] == 0:
            if l[i]:
                l[i] = 0
                on -= 1
            else:
                l[i] = 1
                on += 1
    ans = max(on, ans)

print(ans)
