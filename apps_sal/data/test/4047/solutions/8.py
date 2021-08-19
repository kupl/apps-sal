n = int(input())
(a, b) = (0, 0)
for x in input().split():
    if int(x) % 2 == 0:
        a += 1
    else:
        b += 1
print(min(a, b))
