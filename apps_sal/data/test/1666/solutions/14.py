# coding=utf-8

x, y, a, b = list(map(int, input().split(' ')))
ans = 0
result = ''
for i in range(a, x + 1):
    for j in range(b, y + 1):
        if i > j:
            ans += 1
            result += '%s %s\n' % (i, j)
print(ans)
if ans:
    print(result)

