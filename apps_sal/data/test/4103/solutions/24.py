(n, b, a) = list(map(int, input().split()))
am = a
s = list(map(int, input().split()))
dist = 0
for i in s:
    if i == 0:
        if a > 0:
            a -= 1
            dist += 1
        elif b > 0:
            b -= 1
            dist += 1
        else:
            break
    elif a == am:
        a -= 1
        dist += 1
    elif b > 0:
        b -= 1
        a += 1
        dist += 1
    elif a > 0:
        a -= 1
        dist += 1
print(dist)
