(a, b) = map(int, input().split())
f = str(a) * b
n = str(b) * a
if f > n:
    print(n)
else:
    print(f)
