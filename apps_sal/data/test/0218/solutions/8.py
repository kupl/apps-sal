n, a, b = list(map(int, input().split(' ')))

s = input()

c = 0
while c * a <= n and (n - c * a) % b != 0:
    c += 1

if c * a > n:
    print(-1)
else:
    cb = (n - a * c) // b
    print(c + cb)
    for i in range(c):
        print(s[a * i: a * (i + 1)])
    for i in range(cb):
        print(s[c * a + b * i: c * a + b * (i + 1)])
