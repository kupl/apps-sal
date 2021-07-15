from sys import stdin, stdout

n, s = map(int, stdin.readline().split())

l = 0
r = n + 1
while r - l > 1:
    f = lambda x: sum(map(int, list(str(x))))
    m = (r + l) // 2
    
    if m - f(m) >= s:
        r = m
    else:
        l = m

while r == f(r):
    r += 1


stdout.write(str(max(0, n - r + 1)))
