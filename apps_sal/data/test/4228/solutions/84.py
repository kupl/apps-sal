n, l = map(int, input().split())
s = int(n * (l + n + l - 1) / 2)
if l > 0 and n + l - 1 > 0:
    print(s - l)
elif l < 0 and n + l - 1 < 0:
    print(s - (n + l - 1))
else:
    print(s)
