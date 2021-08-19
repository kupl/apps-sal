n = int(input())
pn = list(map(int, input().split()))
count = 0
for x in range(1, n - 1):
    if pn[x + 1] > pn[x] > pn[x - 1] or pn[x - 1] > pn[x] > pn[x + 1]:
        count += 1
print(count)
