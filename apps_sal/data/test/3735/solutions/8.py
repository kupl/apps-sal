def sum(x):
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res


n = int(input())
ans = 0
for i in range(min(n, 1000)):
    ans = max(ans, sum(i) + sum(n - i))
for i in range(1, 13):
    nine = '9' * i
    for j in range(10):
        tmp = int(str(j) + nine)
        if tmp <= n:
            ans = max(ans, sum(tmp) + sum(n - tmp))
print(ans)
