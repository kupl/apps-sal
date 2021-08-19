n = int(input())
li = list(map(int, input().split()))
prev = None
for (ind, z) in enumerate(reversed(li)):
    if prev is not None:
        if z != prev[1]:
            break
        prev[0] = ind
    else:
        prev = [ind, z]
print(n - prev[0])
