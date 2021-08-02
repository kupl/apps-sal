s = input()
l, *v = (int(x) for x in input().split())
v.sort(reverse=True)
count = 0
while l <= v[0]:
    if len(v) == 1 or v[0] > v[1]:
        count += 1
        l += 1
        v[0] -= 1
    else:
        count += 1
        l += 1
        v[0] -= 1
        v.sort(reverse=True)
print(count)
