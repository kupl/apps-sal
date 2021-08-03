a, b = list(map(int, input().split()))

cnt = 0
plug = 1

if b > 1:
    while plug < b:
        plug = plug - 1 + a
        cnt += 1

print(cnt)
