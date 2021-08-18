import sys

n, m = list(map(int, input().split()))
a, b = list(map(int, input().split()))
pool = [a, b]
pairs = [(a, b)]
for _ in range(m - 1):
    a, b = list(map(int, input().split()))
    if a not in pool and b not in pool:
        pool.append(a)
        pool.append(b)
    pairs.append((a, b))
    if len(pool) >= 5:
        print("NO")
        return
count = 0
for i in range(len(pool) - 1):
    for j in range(i + 1, len(pool)):
        x = [pool[i], pool[j]]
        for k in pairs:
            if k[0] != x[0] and k[0] != x[1] and k[1] != x[0] and k[1] != x[1]:
                count += 1
                break

if count != len(pool) * (len(pool) - 1) // 2:
    print("YES")
else:
    print("NO")
