def read():
    return map(int, input().split())


(n, k) = read()
a = sorted(read())
cur = k
ans = 0
for i in a:
    while cur * 2 < i:
        cur *= 2
        ans += 1
    cur = max(cur, i)
print(ans)
