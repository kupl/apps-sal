n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
m = max(c)
a = []
for i in range(m + 1):
    a.append(c.count(i))
p = [0] * (m + 1)
curmax = 10**9
for i in range(n):
    ind = 0
    best_result = 0
    for j in range(m + 1):
        current_result = 10**9
        for k in range(m + 1):
            mn = p[k]
            if k == j:
                mn += 1
            if mn == 0:
                continue
            current_result = min(current_result, a[k] // mn)
        if current_result > best_result:
            best_result = current_result
            ind = j
    p[ind] += 1
ans = 10**9
for i in range(m + 1):
    if p[i] > 0:
        ans = min(ans, a[i] // p[i])
print(ans)
