a = [0] * 3
a[0], a[1], a[2], t1, t2 = map(int, input().split())
a[0] += a[1] / 60 + a[2] / 3600
a[1] = a[1] / 5 + a[2] / 300
a[2] /= 5
a[0] %= 12
t1 %= 12
t2 %= 12
a = sorted(a)
if t1 > t2:
    t1, t2 = t2, t1
if a[0] < t1 and t2 < a[1]:
    print("YES")
elif a[1] < t1 and t2 < a[2]:
    print("YES")
else:
    if t1 > a[2] and t2 > a[2]:
        print("YES")
    elif t2 > a[2] and t1 < a[0]:
        print("YES")
    elif t1 < a[0] and t2 < a[0]:
        print("YES")
    else:
        print("NO")
