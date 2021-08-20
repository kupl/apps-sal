def rot(s, pos):
    return s[len(s) - pos:] + s[:len(s) - pos]


s = input()
x = int(input())
s = [''] + list(s)
for i in range(x):
    (a, b, c) = list(map(int, input().split(' ')))
    s[a:b + 1] = rot(s[a:b + 1], c % (b - a + 1))
print(''.join(s))
