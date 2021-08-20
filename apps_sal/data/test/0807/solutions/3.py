(n, c) = list(map(int, input().split()))
(last, best) = (-1, 0)
for x in map(int, input().split()):
    t = last - x - c
    best = max(best, t)
    last = x
print(best)
