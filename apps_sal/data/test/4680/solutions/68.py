x = list(map(int, input().split()))
x.sort()
f = True
for i, e in enumerate(x):
    tmp = 5
    if i == 2:
        tmp = 7

    f &= (tmp == e)
print(("YES" if f else "NO"))

