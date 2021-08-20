(a, b, c) = map(int, input().split())
tmp = c - (a - b)
if tmp < 0:
    print(0)
else:
    print(tmp)
