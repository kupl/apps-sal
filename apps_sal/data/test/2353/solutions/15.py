ans = []
for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    if b >= a:
        ans.append(b)
        continue
    a -= b
    if d >= c:
        ans.append(-1)
        continue
    x = (a - 1) // (c - d) + 1
    ans.append(b + x * c)
print('\n'.join(map(str, ans)))
