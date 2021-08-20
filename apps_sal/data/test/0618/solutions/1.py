(a, b) = input().split('|')
c = input()
i = 0
while len(c) > 0:
    if len(a) < len(b):
        a += c[0]
    else:
        b += c[0]
    c = c[1:]
print(['Impossible', a + '|' + b][len(a) == len(b)])
