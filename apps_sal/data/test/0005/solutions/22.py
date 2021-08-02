n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)
elif l == 1:
    print(abs(r - pos) + 1)
elif r == n:
    print(abs(l - pos) + 1)
else:
    print(min(abs(l - pos), abs(r - pos)) + r - l + 2)
