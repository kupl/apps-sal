t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    if (a == b):
        print(0)
    elif (a % 2 == b % 2 and a > b):
        print(1)
    elif (a % 2 != b % 2 and b > a):
        print(1)
    else:
        print(2)

