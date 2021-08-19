(n, a, b) = map(int, input().split())
ans = 0
for i in range(n + 1):
    i = str(i)
    c = 0
    for l in i:
        c += int(l)
    if a <= c and c <= b:
        ans += int(i)
print(ans)
