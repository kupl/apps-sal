n = int(input())
s = input()
g = 'ACTG'
m = 10000000
for i in range(n - 3):
    t = 0
    for j in range(4):
        k = abs(ord(s[i + j]) - ord(g[j]))
        t += min(k, 26 - k)
    m = min(m, t)
print(m)
