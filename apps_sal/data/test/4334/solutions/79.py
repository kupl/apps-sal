s, t = input().split()
a, b = map(int, input().split())
u = str(input())

if u == s:
    print(a - 1, b)
else:
    print(a, b - 1)
