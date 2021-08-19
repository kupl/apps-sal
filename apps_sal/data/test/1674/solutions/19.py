from sys import stdin
(n, m) = list(map(int, stdin.readline().strip().split()))
s = list(map(int, stdin.readline().strip().split()))
s1 = stdin.readline().strip()
x = [s[0]]
cur = s1[0]
y = 1
ans = 0
while y < n:
    if s1[y] == cur:
        x.append(s[y])
    else:
        cur = s1[y]
        if len(x) > m:
            x.sort()
            for i in range(m):
                ans += x[-1]
                x.pop()
        else:
            ans += sum(x)
        x = [s[y]]
    y += 1
if len(x) > m:
    x.sort()
    for i in range(m):
        ans += x[-1]
        x.pop()
else:
    ans += sum(x)
print(ans)
