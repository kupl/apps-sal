n = int(input())
res = prev = 0
for e in sorted(map(int, input().split())):
    if e < prev:
        continue
    res += 1
    if e == prev:
        e += 1
    if e - 1 > prev:
        e -= 1
    prev = e
print(res)
