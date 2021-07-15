n = int(input())
s = set()
ans = 0
for i in map(int, input().split()):
    ans = max(ans, len(s))
    if i in s:
        s -= set([i])
    else:
        s.add(i)
print(ans)
