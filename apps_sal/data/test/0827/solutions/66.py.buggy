N = int(input())
T = input()

if N == 1:
    if T == "0":
        print((10**10))
    else:
        print((10**10 * 2))
    return

if N == 2:
    if T == "00":
        print((0))
    if T == "01":
        print((10**10 - 1))
    if T == "10":
        print((10**10))
    if T == "11":
        print((10**10))
    return

zi = 0
for i in range(3):
    if T[i] == "0":
        zi = i
        break
else:
    print((0))
    return

for i in range(N):
    if i % 3 == zi:
        if T[i] != "0":
            print((0))
            return
    else:
        if T[i] != "1":
            print((0))
            return

m = (N + (3 - zi + 2) % 3 + 2) // 3
print((10**10 - m + 1))
