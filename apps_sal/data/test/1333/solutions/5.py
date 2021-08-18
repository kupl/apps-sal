n, m = list(map(int, input().split()))
i = 0
z = 0
while i < n:
    if i % 2 == 0:
        print("
    else:
        if z % 2 == 0:
            print("." * (m - 1) + "
        else:
            print("
        z += 1
    i += 1
