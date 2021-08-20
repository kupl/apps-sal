def multiple(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        a.append(i * i)
    return a


n = int(input())
a = multiple(n)
ans = 10 ** 18
for i in a:
    if n - i < 0:
        continue
    ans = min(ans, abs(n - i))
print(n - ans)
