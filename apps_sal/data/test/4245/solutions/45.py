A, B = map(int, input().split())

if B == 1:
    print(0)
elif A >= B:
    print(1)
else:
    count = 0
    for n in range(1, 100):
        if A + (A - 1) * n >= B:
            print(n + 1)
            break
