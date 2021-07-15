n = int(input())
prev = u = g = 0
for i in (int(x) for x in input().split()):
    if i == 1:
        u += 1
        if prev == 0:
            g += 1
    prev = i
print(u + g - 1 if u > 0 else 0)
