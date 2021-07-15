m = 10**9+7

s = input()

r = x = 1
for c in s:
    if c == 'b':
        r = (r * x) % m
        x = 1
    elif c == 'a':
        x += 1
r = (r * x) % m

print(r - 1)

