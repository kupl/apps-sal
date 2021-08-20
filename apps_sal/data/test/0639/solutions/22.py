(n, x) = list(map(int, input().split()))
lst = []
for y in input().split():
    lst.append(int(y))
lst.sort()
k = 0
for y in range(0, x):
    if not y in lst:
        k += 1
if x in lst:
    print(k + 1)
else:
    print(k)
