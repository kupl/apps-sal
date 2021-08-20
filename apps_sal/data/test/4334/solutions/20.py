(s, t) = input().split()
(a, b) = map(int, input().split())
u = input()
if s == u or s == t:
    print(a - 1, b)
else:
    print(a, b - 1)
