(c, v0, v1, a, l) = map(int, input().split())
cnt = 0
ans = 0
v = v0
while cnt < c:
    cnt += v
    if ans != 0:
        cnt -= l
    if v + a < v1:
        v += a
    else:
        v = v1
    ans += 1
print(ans)
