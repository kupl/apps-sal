import queue

N = int(input())

def common_divisors(n):
    i = 1
    res = []
    while i*i <= n:
        if n % i == 0:
            res.append(i)
            res.append(n//i)
        if i*i == n:
            res.pop()
        i += 1
    return res

ans = 0
ans += len(common_divisors(N-1))-1

for i in common_divisors(N):
    if i == 1:
        continue
    n = N
    while n % i == 0:
        n /= i
    if n % i == 1:
        ans += 1
print(ans)


