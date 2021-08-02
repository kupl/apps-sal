def step(x):
    res = 0
    while x > 0 and x % 2 ** (res + 1) == 0:
        res += 1
    return res


n = int(input())
x = list(map(int, input().split()))
r = 0
m = 0
for i in range(n):
    if step(x[i]) > r:
        m = 1
        r = step(x[i])
    elif step(x[i]) == r:
        m += 1
print(2 ** r, m)
