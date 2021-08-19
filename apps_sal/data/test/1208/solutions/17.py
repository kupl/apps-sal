n = int(input())
count = [0] * 1000001
cur = 0
ans = 0
for i in range(n):
    (c, d) = input().split()
    d = int(d)
    if c == '-' and count[d]:
        cur -= 1
        count[d] -= 1
    elif c == '-' and (not count[d]):
        ans = ans + 1
    elif c == '+':
        cur += 1
        ans = max(ans, cur)
        count[d] += 1
print(ans)
