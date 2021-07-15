n = int(input())

def f(k, p):
    p = 2 * p - 1
    return p * (2 ** k - 1) + p * (p - 1) // 2

ans = set()

for k in range(65):
    l = 0
    r = n + 2
    while l + 1 < r:
        m = (l + r) // 2
        if f(k, m) < n:
            l = m
        else:
            r = m
    if f(k, r) > n:
        continue
    while f(k, r + 1) == n:
        r += 1
    for i in range(l + 1, r + 1):
        ans.add(2 ** k * (2 * i - 1))
        
for x in sorted(ans):
    print(x)
    
if not ans:
    print(-1)

