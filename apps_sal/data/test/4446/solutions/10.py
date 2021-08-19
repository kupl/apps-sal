(n, a, b, k) = list(map(int, input().split()))
hp = sorted([((int(x) % (a + b) or a + b) + a - 1) // a - 1 for x in input().split()])
score = 0
for h in hp:
    if h <= k:
        k -= h
        score += 1
print(score)
