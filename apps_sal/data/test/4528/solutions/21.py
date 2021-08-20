for i in range(int(input())):
    (h, m) = [int(a) for a in input().split()]
    print(24 * 60 - h * 60 - m)
