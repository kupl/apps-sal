t = int(input())
for case in range(t):
    (r, g, b, w) = list(map(int, input().split()))
    nodd = r % 2 + g % 2 + b % 2 + w % 2
    if nodd == 2:
        print('No')
    elif nodd <= 1:
        print('Yes')
    elif r == 0 or g == 0 or b == 0:
        print('No')
    else:
        print('Yes')
