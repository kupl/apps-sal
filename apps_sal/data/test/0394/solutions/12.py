n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    a[i] -= a[i - 1]

lens = []
for l in range(1, n + 1):
    f = True
    for i in range(n):
        if a[i] != a[i % l]:
            f = False
    if f:
        lens.append(l)

print(len(lens))
for i in lens:
    print(i, end=" ")
