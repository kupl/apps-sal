(n, s) = [int(w) for w in input().split()]
r = 0
for _ in range(n):
    (h, m) = [int(w) for w in input().split()]
    t = 60 * h + m
    if t > r + s:
        break
    r = t + s + 1
print(r // 60, r % 60)
