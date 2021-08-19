(n, k) = tuple(map(int, input().split()))
a = []
for i in range(n):
    a.append(input())
r = 0
for s in a:
    f = True
    for i in range(k + 1):
        if str(i) not in s:
            f = False
            break
    if f:
        r = r + 1
print(r)
