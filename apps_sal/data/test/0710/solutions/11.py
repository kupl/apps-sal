n = int(input())
s = input()
g = 'ACTG'
res = float('inf')
for i in range(n - 3):
    val = 0
    for j in range(4):
        kek = abs(ord(g[j]) - ord(s[i + j]))
        val += min(kek, 26 - kek)
    res = min(res, val)
print(res)
