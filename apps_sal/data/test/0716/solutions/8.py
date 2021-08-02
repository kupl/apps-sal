read = lambda: list(map(int, input().split()))
n, a, b = read()
s = ' ' + input()
if s[a] == s[b]:
    print(0)
    return
else:
    print(1)
