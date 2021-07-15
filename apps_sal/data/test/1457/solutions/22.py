a = input().rstrip()
b = input().rstrip()

def prefix_fn(string, pattern):
    s = pattern + "$" + string
    p = [0] * len(s)
    k = 0
    for i, c in enumerate(s[1:], 1):
        while s[k] != c and k > 0:
            k = p[k-1]
        if s[k] == c:
            k += 1
        p[i] = k
    return p[len(pattern)+1:]

last_occ = -1
m = len(b)
count = 0
for i, c in enumerate(prefix_fn(a, b)):
    if last_occ != -1:
        last_occ += 1
    if c == m and (last_occ >= m or last_occ == -1):
        count += 1
        last_occ = 0

print(count)

