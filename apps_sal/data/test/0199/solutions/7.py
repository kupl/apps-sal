(n, s) = map(int, input().split())
a = list(map(int, input().split()))
y = min(a) * n
x = sum(a)
if x < s:
    print(-1)
elif s <= x - y:
    print(y // n)
else:
    s = s - (x - y)
    print((y - s) // n)
