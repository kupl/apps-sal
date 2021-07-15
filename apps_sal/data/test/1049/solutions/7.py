n, d = map(int, input().split())
result = 0
cur = 0

for i in range(d):
    if '0' in input():
        cur += 1
    else:
        cur = 0
    result = max(result, cur)


print(result)
