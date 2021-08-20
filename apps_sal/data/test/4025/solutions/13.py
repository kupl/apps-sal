(a, b, c) = list(map(int, input().split()))
d = min(a // 3, b // 2, c // 2)
p = [0] * 3
p[0] = a - 3 * d if d > 0 else a
p[1] = b - 2 * d if d > 0 else b
p[2] = c - 2 * d if d > 0 else c
r = [0, 1, 2, 0, 2, 1, 0] * 2
i = 0
j = 0
ans = 0
while i < 14 and j < 14:
    if p[r[j]]:
        p[r[j]] -= 1
        j += 1
    elif i != j:
        p[r[i]] += 1
        i += 1
    else:
        i += 1
        j += 1
    ans = max(ans, j - i)
print(d * 7 + ans)
