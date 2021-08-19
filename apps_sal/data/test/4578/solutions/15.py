(n, x) = map(int, input().split())
m = []
for i in range(n):
    a = int(input())
    x -= a
    m.append(a)
ans = min(m)
x = x // ans
print(x + n)
