(a1, a2) = list(map(int, input().split()))
n = 0
while a1 >= 1 and a2 > 1 or (a1 > 1 and a2 >= 1):
    if a1 < a2:
        a1 += 1
        a2 -= 2
    else:
        a1 -= 2
        a2 += 1
    n += 1
print(n)
