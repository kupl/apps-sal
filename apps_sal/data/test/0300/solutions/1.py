n = int(input())
a = list(map(int, input().split()))
c = [0, 0, 0, 0, 0, 0]
for _ in a:
    c[_] += 1
s = sum(a)
ans = 0
while 2 * s < 9 * n:
    if c[2] > 0:
        s += 3
        c[2] -= 1
        c[5] += 1
        ans += 1
    elif c[3] > 0:
        s += 2
        c[3] -= 1
        c[5] += 1
        ans += 1
    elif c[4] > 0:
        s += 1
        c[4] -= 1
        c[5] += 1
        ans += 1
print(ans)
