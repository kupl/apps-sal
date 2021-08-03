s = input()
r = s.index('R') % 4
b = s.index('B') % 4
y = s.index('Y') % 4
g = s.index('G') % 4
ans = [0] * 4
for i in range(0, len(s)):
    if(s[i] == '!'):
        ans[i % 4] += 1
print('%d %d %d %d' % (ans[r], ans[b], ans[y], ans[g]))
