n = int(input())
arr = list(map(int, input().split()))

counter_negative = 0
current = 0

res = []

for a in arr:
    current += 1
    if a < 0:
        counter_negative += 1

    if counter_negative == 3:
        res.append(current-1)
        current = 1
        counter_negative = 1
res.append(current)

print(len(res))
for r in res:
    print(r, end=' ')

