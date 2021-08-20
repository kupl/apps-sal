t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if '>' in s:
        left = s.index('>')
    else:
        left = n + 1
    if '<' in s:
        right = s[::-1].index('<')
    else:
        right = n + 1
    print(min(left, right))
