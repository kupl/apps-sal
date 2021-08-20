n = int(input())
is_prime = [True for _ in range(100)]
is_prime[0] = is_prime[1] = False
for i in range(100):
    if not is_prime[i]:
        continue
    for j in range(i * i, 100, i):
        if not is_prime[j]:
            is_prime[j] = False
factor = [0 for _ in range(100)]
for i in range(2, n + 1):
    for j in range(2, 100):
        if is_prime[j]:
            while i % j == 0:
                factor[j] += 1
                i //= j
fs = []
for i in range(100):
    if factor[i] != 0:
        fs.append(factor[i])
m = len(fs)
ans = [0 for _ in range(4)]
for i in range(m):
    for j in range(m):
        for k in range(m):
            if i != j and j != k and (k != i):
                if fs[i] >= 4 and fs[j] >= 4 and (fs[k] >= 2):
                    ans[0] += 1
for i in range(m):
    if fs[i] >= 74:
        ans[1] += 1
for i in range(m):
    for j in range(m):
        if i != j:
            if fs[i] >= 2 and fs[j] >= 24:
                ans[2] += 1
for i in range(m):
    for j in range(m):
        if i != j:
            if fs[i] >= 4 and fs[j] >= 14:
                ans[3] += 1
Ans = ans[0] // 2 + ans[1] + ans[2] + ans[3]
print(Ans)
