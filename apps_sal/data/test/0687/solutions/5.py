(a, b) = list(map(int, input().split()))
if a == b:
    print(a * 10, a * 10 + 1)
elif a != 9:
    if b - a == 1:
        print(a, b)
    else:
        print(-1)
elif b == 1:
    print(9, 10)
else:
    print(-1)
