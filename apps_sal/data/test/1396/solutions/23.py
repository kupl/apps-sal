(n, k, x) = map(int, input().split())
balls = list(map(int, input().split()))
c = 0
p = None
pairs = []
matches = []
for b in range(len(balls)):
    if balls[b] is not c:
        c = balls[b]
    if c is p:
        pairs.append((b - 1, b))
        if c is x:
            matches.append((b - 1, b))
    p = c
max = 0
for m in matches:
    (i, j) = m
    removed = 2
    i -= 1
    j += 1
    while i >= 0 and j < len(balls):
        if balls[i] is balls[j]:
            toRemove = 0
            if j < len(balls) - 1 and balls[j + 1] is balls[j]:
                toRemove += 1
                j += 1
            if i >= 1 and balls[i - 1] is balls[i]:
                toRemove += 1
                i -= 1
            if toRemove > 0:
                removed += toRemove + 2
            else:
                break
        else:
            break
        i -= 1
        j += 1
    if removed > max:
        max = removed
print(max)
