t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    a1 = 0
    for x in a:
        if x % 2 == 0:
            a1 += 1
    b1 = 0
    for x in b:
        if x % 2 == 0:
            b1 += 1
    print(a1 * b1 + (len(a) - a1) * (len(b) - b1))

