n = int(input())
s = list(input())
ans = 0
for i in range(1, n):
    count = 0
    x = sorted(set(s[:i]))
    y = sorted(set(s[i:]))
    for j in x:
        if j in y:
            count += 1
    ans = max(ans, count)
print(ans)
