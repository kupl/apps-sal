t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a, b = 999999999, 9999999999
    if '>' in s:
        a = s.index('>')
    if '<' in s:
        b = n - 1 - s.rindex('<')
    print(min(a, b))
