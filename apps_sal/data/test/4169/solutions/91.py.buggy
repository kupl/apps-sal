n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab_s = sorted(ab)

res = m
temp = 0

for i in range(n):
    if res <= ab_s[i][1]:
        temp += res * ab_s[i][0]
        print(temp)
        return
    else:
        temp += ab_s[i][1] * ab_s[i][0]
        res -= ab_s[i][1]
