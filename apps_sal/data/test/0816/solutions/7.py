n, x = list(map(int, input().split()))
A = list(map(int, input().split()))
d1 = {}
for a in A:
    if a in d1:
        d1[a] += 1
    else:
        d1[a] = 1

keys = list(d1.keys())
keys.sort()
ans = 0
for k in keys:
    b = k ^ x
    if b > k:
        if b in d1:
            ans += d1[b] * d1[k]
    elif b == k:
        ans += d1[b] * (d1[b] - 1) // 2

print(ans)
