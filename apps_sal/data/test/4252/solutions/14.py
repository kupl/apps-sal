n = int(input())
s = input()

ans = 0
while 'xxx' in s:
    ind = s.index('xxx')
    s = list(s)
    s[ind: ind + 3] = ['x', 'x']
    s = ''.join(s)
    ans += 1

print(ans)
