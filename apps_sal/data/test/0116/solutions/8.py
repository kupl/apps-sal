from sys import stdout
(a, b, c, d, e) = [int(i) for i in input().split()]
t = max(a, c)
t1 = min(b, d)
if t <= t1:
    if t <= e and e <= t1:
        print(t1 - t)
    else:
        print(t1 - t + 1)
else:
    print(0)
