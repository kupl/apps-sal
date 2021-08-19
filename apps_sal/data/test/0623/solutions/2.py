(a1, a2) = list(map(int, input().split()))
c = 0
while a1 > 1 and a2 > 0 or (a2 > 1 and a1 > 0):
    if a1 >= a2:
        a1 -= 2
        a2 += 1
    else:
        a1 += 1
        a2 -= 2
    c += 1
print(c)
