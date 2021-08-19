# len(set) 愚直
n = int(input())
s = list(input())
ans = 0
for i in range(1, n):
    x, y = set(s[:i]), set(s[i:])
    ans = max(ans, len(x & y))
print(ans)
