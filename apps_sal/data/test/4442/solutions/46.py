(a, b) = map(int, input().split())
s = [a] * b
t = [b] * a
ab = map(str, s)
ba = map(str, t)
if a <= b:
    print(''.join(ab))
else:
    print(''.join(ba))
