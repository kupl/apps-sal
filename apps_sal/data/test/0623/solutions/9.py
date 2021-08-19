(a1, a2) = list(map(int, input().strip().split()))
count = 0
while a1 > 0 and a2 > 0:
    if a1 <= a2:
        a1 += 1
        a2 -= 2
    else:
        a2 += 1
        a1 -= 2
    if a1 >= 0 and a2 >= 0:
        count += 1
    if a1 == 0 or a2 == 0:
        break
print(count)
