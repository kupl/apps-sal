(n, b, d) = [int(x) for x in input().split()]
cur = 0
count = 0
xs = [int(x) for x in input().split()]
for i in xs:
    if i > b:
        continue
    else:
        cur += i
        if cur > d:
            count += 1
            cur = 0
print(count)
