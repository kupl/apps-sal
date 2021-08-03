s = input()
if '.' not in s:
    s = s + '.'
s = '0' + s + '0'
dp = s.find('.')
pre = s[0:dp]
post = s[dp + 1:]
i = 0
while i < len(pre) - 1 and pre[i] == '0':
    i += 1
pre = pre[i:]
i = len(post) - 1
while i > 0 and post[i] == '0':
    i -= 1
post = post[:i + 1]
b = 0
if pre == '0':
    b -= len(post)
    pre = post
    post = '0'
    i = 0
    while i < len(pre) - 1 and pre[i] == '0':
        i += 1
    pre = pre[i:]
b += len(pre) - 1
post = pre[1:] + post
pre = pre[0]
i = len(post) - 1
while i > 0 and post[i] == '0':
    i -= 1
post = post[:i + 1]
if post == '0' or post == '':
    print(pre, end='')
else:
    print(pre + '.' + post, end='')
if b != 0:
    print('E' + str(b), end='')
print('')
