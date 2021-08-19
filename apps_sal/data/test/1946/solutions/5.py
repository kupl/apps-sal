n = int(input())
s = {}
for i in range(n):
    (a, b) = list(map(int, input().split()))
    s[a] = b
m = int(input())
for j in range(m):
    (a, b) = list(map(int, input().split()))
    if a in s:
        s[a] = max(s[a], b)
    else:
        s[a] = b
ans = 0
for i in s:
    ans += s[i]
print(ans)
