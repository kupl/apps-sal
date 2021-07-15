n, a, b = map(int, input().split())
s = input().strip()
if (s[a - 1] == s[b - 1]):
    print(0)
else:
    print(1)
