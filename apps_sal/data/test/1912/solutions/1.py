for t in range(int(input())):
    r, g, b, w = list(map(int, input().split()))
    if r == 0 or g == 0 or b == 0:
        if r % 2 + g % 2 + b % 2 + w % 2 <= 1:
            print("Yes")
        else:
            print("No")
    else:
        if r % 2 + g % 2 + b % 2 + w % 2 == 2:
            print("No")
        else:
            print("Yes")
