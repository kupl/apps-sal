(n, l) = map(int, input().split())
s = int(n * (2 * l + n - 1) / 2)
if l <= 0 and l + n - 1 >= 0:
    print(s)
elif l <= 0:
    print(s - l - n + 1)
else:
    print(s - l)
