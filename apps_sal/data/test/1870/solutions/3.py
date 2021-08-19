(n, c) = list(map(int, input().split()))
cnt = last = 0
for x in map(int, input().split()):
    if x > last + c:
        cnt = 1
    else:
        cnt += 1
    last = x
print(cnt)
