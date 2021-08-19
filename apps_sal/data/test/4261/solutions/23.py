(a, b, c) = list(map(int, input().split()))
d = a - b
e = c - d
if e < 0:
    e = 0
print(e)
