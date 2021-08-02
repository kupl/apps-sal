n = int(input())
ww = list(map(int, input().split()))
ans = 9999999999999999
for t in range(1, n):
    s1 = 0
    s2 = 0
    for j in range(n):
        if (j + 1) <= t:
            s1 += ww[j]
        else:
            s2 += ww[j]
    ans = min(ans, abs(s1 - s2))
print(ans)
