n, m = map(int, input().split())
mxx, mxy, mnx, mny = 0, 0, n + 1, m + 1
for i in range(0, n):
    line = input()
    for j in range(0, m):
        if line[j] == '*':
            mxx = max(mxx, i)
            mxy = max(mxy, j)
            mnx = min(mnx, i)
            mny = min(mny, j)
print(max(mxx - mnx + 1, mxy - mny + 1))
