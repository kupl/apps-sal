n = input()
cur = 0
cnt = 0
for i in map(int, input().split()):
    c = 0
    while i % 2 == 0:
        i >>= 1
        c += 1
    if c > cur:
        cur = c
        cnt = 1
    elif c == cur:
        cnt += 1
print(2 ** cur, cnt)
