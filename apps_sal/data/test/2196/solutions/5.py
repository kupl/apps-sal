from sys import stdin, stdout
n = int(stdin.readline())
t = list(map(int, stdin.readline().split()))
y = s = t[0]
x = i = 1
while True:
    while i < n and t[i] == y:
        i += 1
        x += 1
    s += x + 1 & 1
    x //= 2
    y += 1
    if x:
        continue
    if i == n:
        break
    s += t[i] - y
    (x, y) = (1, t[i])
    i += 1
print(s)
