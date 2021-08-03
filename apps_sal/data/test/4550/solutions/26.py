a, b, c = map(int, input().split())

s = sum([a, b, c])
m = max(a, b, c)

if m == (s - m):
    print("Yes")
else:
    print("No")
