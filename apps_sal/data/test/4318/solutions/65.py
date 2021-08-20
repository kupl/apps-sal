n = int(input())
hl = list(map(int, input().split()))
cnt = 0
hmax = 0
for h in hl:
    if hmax <= h:
        hmax = h
        cnt += 1
print(cnt)
