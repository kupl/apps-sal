n = int(input())
s = [x for x in input()]
length = len(s)
i = 0
ans = 0
while i < len(s):
    while i + 2 < len(s) and s[i] == 'x' and (s[i + 1] == 'x') and (s[i + 2] == 'x'):
        ans += 1
        s.pop(i)
    i += 1
print(ans)
