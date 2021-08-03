a, b, c = sorted(list(map(int, input().split())))
cnt = 0
while b < c:
    a += 1
    b += 1
    cnt += 1
while a < c:
    a += 2
    cnt += 1
print(cnt if a == c else cnt + 1)
