t = int(input())
for j in range(t):
    inp = [int(n) for n in input().split()]
    n = inp[0]
    k = inp[1]
    d1 = inp[2]
    d2 = inp[3]
    if d2 < d1:
        s = d1
        d1 = d2
        d2 = s
    if k >= 2 * d1 + d2 and (k - 2 * d1 - d2) % 3 == 0 and (n - k >= d1 + 2 * d2) and ((n - k - d1 - 2 * d2) % 3 == 0):
        print('yes')
    elif k >= 2 * d2 + d1 and (k - 2 * d2 - d1) % 3 == 0 and (n - k >= d2 + 2 * d1) and ((n - k - d2 - 2 * d1) % 3 == 0):
        print('yes')
    elif k >= d1 + d2 and (k - d1 - d2) % 3 == 0 and (n - k >= 2 * d2 - d1) and ((n - k - 2 * d2 + d1) % 3 == 0):
        print('yes')
    elif k >= 2 * d2 - d1 and (k - 2 * d2 + d1) % 3 == 0 and (n - k >= d1 + d2) and ((n - k - d1 - d2) % 3 == 0):
        print('yes')
    else:
        print('no')
