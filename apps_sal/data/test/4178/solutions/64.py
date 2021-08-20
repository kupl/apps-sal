n = int(input())
h = list(map(int, input().split()))
if n == 1:
    print('Yes')
elif n == 2:
    if h[0] - h[1] <= 1:
        print('Yes')
    else:
        print('No')
else:
    c = 0
    if h[0] - h[1] <= 1:
        h[0] -= 1
        for i in range(1, n - 1):
            if h[i] - h[i + 1] == 1 and h[i - 1] < h[i]:
                h[i] -= 1
                c += 1
            elif h[i] <= h[i + 1] and h[i - 1] < h[i]:
                h[i] -= 1
                c += 1
            elif h[i] <= h[i + 1]:
                c += 1
            else:
                break
    if c == n - 2:
        print('Yes')
    else:
        print('No')
