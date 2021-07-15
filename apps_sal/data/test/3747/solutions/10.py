q = input()
p = [0] * 250
for i in q:
    p[ord(i)] += 1
ans = p[ord('B')]
ans = min(ans, p[ord('u')] // 2)
ans = min(ans, p[ord('a')] // 2)
ans = min(ans, p[ord('s')])
ans = min(ans, p[ord('b')], p[ord('l')], p[ord('r')])
print(ans)
