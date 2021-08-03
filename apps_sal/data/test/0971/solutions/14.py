n, b, d = list(map(int, input().split()))
v = 0
cnt = 0
for cur in map(int, input().split()):
    if cur <= b:
        v += cur
        if v > d:
            v = 0
            cnt += 1
print(cnt)
