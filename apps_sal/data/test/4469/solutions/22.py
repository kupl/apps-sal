q = int(input())
dc = dict()
l = 0
r = 0
z, n = input().split()
n = int(n)
dc[n] = l
for i in range(q - 1):
    z, n = input().split()
    n = int(n)
    if z == 'L':
        l -= 1
        dc[n] = l
    elif z == 'R':
        r += 1
        dc[n] = r
    else:
        print(min(dc[n] - l, r - dc[n]))

