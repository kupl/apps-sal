n = int(input())
prime = [0, 0] + [1] * 99999
ans = [0] * 100001
newcnt = 1
for i in range(2, n + 1):
    if prime[i] == 0:
        continue
    ans[i] = newcnt
    t = 2
    while i * t <= n:
        prime[i * t] = 0
        ans[i * t] = newcnt
        t += 1
    newcnt += 1
print(*(ans[2:n + 1]))
