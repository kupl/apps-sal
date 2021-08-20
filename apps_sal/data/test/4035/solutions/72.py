from math import floor
(a, b) = map(int, input().split(' '))
d = False
for p in range(1009):
    if floor(p * 0.08) == a and floor(p * 0.1) == b:
        print(p)
        d = True
        break
if not d:
    print(-1)
