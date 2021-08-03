n = int(input())
sl = list(input() for _ in range(n))
m = int(input())
tl = list(input() for _ in range(m))

cnt = 0
for s in sl:
    cnt = max(cnt, sl.count(s) - tl.count(s))

print(cnt)
