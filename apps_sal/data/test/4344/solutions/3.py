n, k = map(int, input().split())
ar = list(map(int, input().split()))
s = set()
for x in ar:
    s.add(x)
if(len(s) >= k):
    print("YES")
    e = set()
    a = []
    i = 0
    for x in ar:
        i += 1
        if(x not in e):
            a.append(i)
        e.add(x)
    print(*a[:k])
else:
    print("NO")
