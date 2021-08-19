(n, k) = map(int, input().split())
a = []
d = []
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))
mem = 0
for i in range(1, n + 1):
    check = False
    for j in range(k):
        if i in a[j]:
            check = True
    if not check:
        mem += 1
print(mem)
