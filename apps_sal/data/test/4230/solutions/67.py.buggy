x, n = map(int, input().split())
p = list(map(int, input().split()))

a = [i for i in range(102)]

b = list(set(a) - set(p))
ans = 100
for i in range(len(b)):
    c = abs(b[i] - x)
    ans = min(ans, c)

up = x + ans
down = x - ans

if up in set(p):
    print(down)
    return
elif down in set(p):
    print(up)
    return
print(min(up, down))
