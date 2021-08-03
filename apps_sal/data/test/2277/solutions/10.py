n = int(input())

lst = []
for x in input().split():
    lst.append(int(x))

m = int(input())
pair = []
for x in range(m):
    (l, r) = list(map(int, input().split()))
    pair.append((l, r))

k = 0
for x in range(0, len(lst) - 1):
    for y in range(x + 1, len(lst)):
        if lst[y] < lst[x]:
            k += 1

for (l, r) in pair:
    if (k - (r - l + 1) // 2) % 2 == 0:
        print("even")
    else:
        print("odd")
    k = k - (r - l + 1) // 2
