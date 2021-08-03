n, m, x = map(int, input().split())

a = list(map(int, input().split()))

r = 0
l = 0

for i in a:
    if i > x:
        r += 1
    elif i < x:
        l += 1

print(min(l, r))
