n, k = map(int, input().split())
s, d = 0, n // k
t = input()[:: 2]
for i in range(k):
    p = t[i :: k].count('1')
    s += min(d - p, p)
print(s)
