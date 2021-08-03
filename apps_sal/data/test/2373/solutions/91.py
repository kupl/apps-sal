n = int(input())
l = list(map(int, input().split()))
c = 0
for i, p in enumerate(l):
    if i + 1 == p:
        if i != n - 1:
            l[i + 1] = p
        c += 1
print(c)
