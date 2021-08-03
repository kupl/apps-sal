n, a, b = map(int, input().split())
s = input()
k = s[a - 1]
t = s[b - 1]
if k == t:
    print(0)
else:
    print(1)
