(n, k) = list(map(int, input().split()))

lst = []
for x in input().split():
    lst.append(int(x))

i = 0
for x in lst:
    if k % x == 0:
        i = max(i, x)

print(k // i)

