t = int(input())
for case in range(t):
    (a, b) = [int(x) for x in input().split(' ')]
    s = input()
    n = len(s)
    for j in range(2):
        for i in range(len(s)):
            if s[i] != '0':
                break
        s = s[i:]
        s = s[::-1]
    if s == '0':
        s = ''
    y = [u for u in s.split('0') if u]
    c = len(y) * a
    x = [u for u in s.split('1') if u]
    for z in x:
        if len(z) * b < a:
            c -= a
            c += len(z) * b
    print(c)
