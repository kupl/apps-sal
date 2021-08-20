import math
n = int(input())
a = []
end = math.floor(n ** 0.5) + (1 if math.floor(n ** 0.5) ** 2 == n else 0)
for i in range(1, end + 1):
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
ans = []
for i in a:
    m = n // i
    ans.append(m + i * (m - 1) * m // 2)
print(' '.join([str(i) for i in sorted(ans)]))
