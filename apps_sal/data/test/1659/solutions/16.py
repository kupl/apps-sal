n, x = map(int, input().split())
cnt = 0
for i in range(n):
    sgn, v = input().split()
    v = int(v)
    if sgn == "+":
        x += v
    if sgn == "-":
        if x >= v:
            x -= v
        else:
            cnt += 1
print(x, cnt)
