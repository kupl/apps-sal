t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    if a == b:
        print(0)
    elif a % 2 == b % 2:
        if a > b:
            print(1)
        else:
            print(2)
    elif a > b:
        print(2)
    else:
        print(1)
