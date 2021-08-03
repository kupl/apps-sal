a, b = list(map(int, input().split()))
if a < b:
    print(-1)
elif a == b:
    print(a)
else:
    ku = (a - b) // (2 * b)
    kd = (a + b) // (2 * b)
    xd = (a + b) / (2 * kd)
    if ku == 0:
        print(xd)
    else:
        xu = (a - b) / (2 * ku)
        print(min(xu, xd))
