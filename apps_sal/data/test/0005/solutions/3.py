n, pos, l, r = map(int, input().split())
if (l <= pos <= r):
    if (l == 1 and r == n):
        print(0)
    elif (l == 1 and r < n):
        print(r - pos + 1)
    elif (r == n and l > 1):
        print(pos - l + 1)
    else:
        print(r - l + min(r - pos, pos - l) + 2)
elif (pos < l):
    if (r == n):
        print(l - pos + 1)
    else:
        print(r - pos + 2)
elif (pos > r):
    if (l == 1):
        print(pos - r + 1)
    else:
        print(pos - l + 2)
