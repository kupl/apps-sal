A, B = map(int, input().split())

if B == 1:
    print(0)

elif A >= B:
    print(1)

else:
    for i in range(1, B):
        if B <= 1 + (A - 1) * i:
            print(i)
            return
