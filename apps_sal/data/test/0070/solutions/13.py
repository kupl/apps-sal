(n, k) = [int(x) for x in input().split()]
s = str(n)
ans = 0
nulls = 0
f = False
for i in range(len(s) - 1, -1, -1):
    if s[i] != '0':
        ans += 1
    else:
        nulls += 1
    if k == nulls:
        f = True
        ans = len(s) - i - nulls
        break
if f:
    print(ans)
else:
    print(len(s) - 1)
