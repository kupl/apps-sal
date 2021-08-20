def getrazn(ar):
    e = 0
    for i in range(len(ar)):
        if ar[i] - ar[i - 1] > e:
            e = ar[i] - ar[i - 1]
    return e


input()
a = list(map(int, input().split()))
ranz = []
for i in range(1, len(a) - 1):
    acopy = a.copy()
    del acopy[i]
    ranz.append(getrazn(acopy))
print(min(ranz))
