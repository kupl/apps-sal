(n, m) = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
for i in arr:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
days = 1
while True:
    count = 0
    for i in d.keys():
        count += d[i] // days
    if count < n:
        break
    days += 1
print(days - 1)
