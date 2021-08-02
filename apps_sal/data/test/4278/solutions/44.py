n = int(input())

count = 0
sn = {}
for i in range(n):
    s = list(input())
    check = "".join(sorted(s))
    if not check in sn:
        sn[check] = 1
    else:
        count += sn[check]
        sn[check] += 1

print(count)
