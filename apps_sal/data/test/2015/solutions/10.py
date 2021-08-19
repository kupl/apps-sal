for _ in range(int(input())):
    (r, g, b) = sorted(map(int, input().split()))
    if r + g + 1 < b:
        print('No')
    else:
        print('Yes')
