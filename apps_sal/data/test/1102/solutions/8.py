n, a = list(map(int, input().split()))
s = list(map(int, input().split()))
a -= 1
if s[a] == 1:
    ans = -1
else:
    ans = 0
for i in range(n):
    p1 = a - i
    p2 = a + i
    if p1 >= 0 and s[p1] == 1:
        c = 1
    else:
        c = 0
    if p2 < n and s[p2] == 1:
        c += 1
    if c == 2:
        ans += 2
    elif (c == 1 and p1 < 0) or (c == 1 and p2 >= n):
        ans += 1
print(ans)

