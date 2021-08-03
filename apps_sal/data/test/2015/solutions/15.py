t = int(input())
for i in range(t):
    rgb = list(map(int, input().split()))
    rgb.sort()
    if rgb[2] - 1 > rgb[0] + rgb[1]:
        print('No')
    else:
        print('Yes')
