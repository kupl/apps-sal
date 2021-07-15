n = int(input())
p = list(map(int, input().split()))

ps = p.copy()
ps.sort()
dp = dict()
ds = dict()
for i in range(n):
    if p[i] in dp:
        dp[p[i]] += [i]
    else:
        dp[p[i]] = [i]
        ds[p[i]] = 0

lop = []

for i in range(n):
    if p[i] != ps[i]:
        a = i
        b = dp[ps[i]][ds[ps[i]]]
        if abs(b - a) >= n//2:
            lop.append([a+1, b+1])
        else:
            if a < n//2 and b < n//2:
                bl = [n]
            elif a >= n//2 and b >= n//2:
                bl = [1]
            elif a < n//2:
                bl = [n, 1]
            else:
                bl = [1, n]
            if len(bl) == 2:
                lop.append([a+1, bl[0]])
                lop.append([bl[0], bl[1]])
                lop.append([bl[1], b+1])
                lop.append([bl[0], bl[1]])
                lop.append([a+1, bl[0]])
            else:
                lop.append([a+1, bl[0]])
                lop.append([b+1, bl[0]])
                lop.append([a+1, bl[0]])
        p[a], p[b] = p[b], p[a]
        dp[p[a]][ds[p[a]]], dp[p[b]][ds[p[b]]] = dp[p[b]][ds[p[b]]], dp[p[a]][ds[p[a]]]
    ds[p[i]] += 1

print(len(lop))
for op in lop:
    print(*op)

