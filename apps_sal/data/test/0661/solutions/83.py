m, k = list(map(int, input().split()))

if k >= 2**m:
    print((-1))
    return

if m == 0:
    print((0, 0))
    return
if m == 1:
    if k == 0:
        print((0, 0, 1, 1))
        return
    else:
        print((-1))
        return

A = [k]
for i in range(2**m):
    if i == k:
        continue
    A.append(i)
A.append(k)
for i in range(2**m - 1, -1, -1):
    if i == k:
        continue
    A.append(i)

print((*A))
