n, k = map(int, input().split())
mas = list(map(int, input().split()))
ans = 0
for b in range(k):
    m = 0
    for i in range(n):
        if i % k == b:
            continue
        m += mas[i]
    ans = max(ans, abs(m))
print(ans)
