s = input().rstrip()
for i in range(ord('a'), ord('z') + 1):
    s = 'z'.join(s.split(chr(i)))
s = list(s.split('z'))
ans = 0
ans2 = 0
for i in s:
    if len(i) == 0:
        continue
    q = i.split('.')
    if len(q) == 1 or len(q[-1]) == 3:
        ans += int(''.join(q))
    else:
        ans += int(''.join(q[:len(q) - 1]))
        ans2 += int(q[-1])
ans += ans2 // 100
ans2 %= 100
d = ''
if ans2 != 0:
    d = str(ans2)
    d = '.' + '0' * (2 - len(d)) + d
a = []
ans = int(ans)
while ans >= 1000:
    a.append('.' + '0' * (3 - len(str(ans % 1000))) + str(ans % 1000))
    ans //= 1000
a.append(str(ans))
a.reverse()
print(''.join(a) + d)
