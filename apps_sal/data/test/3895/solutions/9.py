n = int(input())
a = list(map(int, input().split()))
i = 0
h = dict()
g = []
for x in a:
    cur = x
    if a[cur - 1] != cur:
        print("-1")
        quit()
    if not h.__contains__(cur):
        h[cur] = len(g)
        g.append(cur)
print(len(g))
for x in a:
    print(h[x] + 1, end=" ")
print()
for x in g:
    print(x, end=" ")

