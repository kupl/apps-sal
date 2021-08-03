n = int(input())

s = input()

ans = 0
ss = set()

for c in s:
    if c.isupper():
        ans = max(ans, len(ss))
        ss = set()
    else:
        ss.add(c)
ans = max(ans, len(ss))
print(ans)
