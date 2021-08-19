n = int(input())
s = input()
(cnt0, cnt1) = (0, 0)
for i in s:
    if i == '0':
        cnt0 += 1
    else:
        cnt1 += 1
if cnt0 != cnt1:
    print('1\n%s' % s)
else:
    print('2')
    print(s[0], s[1:])
