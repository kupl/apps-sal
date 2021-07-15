n = int(input())
a = list(map(int, input().split()))

result = 1
cur = 1
prev = a[0]
for x in a[1:]:
    if x >= prev:
        cur += 1
    else:
        cur = 1
    result = max(result, cur)
    prev = x
print(result)

