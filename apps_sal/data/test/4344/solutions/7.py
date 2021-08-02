a = [int(x) for x in input().strip().split(" ")]

N = a[0]
n = a[1]

l = [int(x) for x in input().strip().split(" ")]
assert len(l) == N

d = {}

for (i, e) in enumerate(l):
    if e not in d:
        d[e] = i + 1


if len(d) >= n:
    print("YES")
    for e in list(d.values())[:n]:
        print(e, end=" ")
else:
    print("NO")
