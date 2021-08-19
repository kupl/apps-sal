from sys import stdin, stdout
(value, power) = stdin.readline().split('e')
ans = value[:value.index('.')] + value[value.index('.') + 1:min(len(value), value.index('.') + int(power) + 1)]
if len(value) <= value.index('.') + int(power) + 1:
    ans += '0' * (int(power) - len(value[value.index('.') + 1:]))
else:
    ans += '.' + value[value.index('.') + int(power) + 1:]
if ans.count('.'):
    (u, r) = ans.split('.')
    if r.count('0') != len(r):
        ans = str(int(u)) + '.' + r
    else:
        ans = str(int(u))
else:
    ans = str(int(ans))
stdout.write(ans)
