t = int(input())
for i in range(t):
    (a, b) = map(int, input().split())
    if a == b:
        print(0)
    elif a & 1 == b & 1:
        if a < b:
            print(2)
        else:
            print(1)
    elif a < b:
        print(1)
    else:
        print(2)
