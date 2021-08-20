(a1, a2) = map(int, input().split())
counter = 0
while True:
    if a1 <= 0 or a2 <= 0:
        break
    else:
        if a2 < a1:
            (a1, a2) = (a2, a1)
        if a2 == 1:
            break
        a1 += 1
        a2 -= 2
        counter += 1
print(counter)
