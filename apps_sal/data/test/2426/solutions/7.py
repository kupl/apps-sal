t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) < 2 and a[0] % 2 == 1:
        print(-1)
    else:
        if a[0] % 2 == 0:
            print(1)
            print(1)
        elif a[1] % 2 == 0:
            print(1)
            print(2)
        else:
            print(2)
            print(1, 2)
