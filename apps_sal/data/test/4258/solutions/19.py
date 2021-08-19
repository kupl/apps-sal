(a, b, t) = map(int, input().split())
time = t + 0.5
num = 0
cnt = 1
mtime = cnt * a
while float(mtime) < time:
    num += b
    cnt = cnt + 1
    mtime = cnt * a
print(num)
