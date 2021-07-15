n = int(input())
a = list(map(int, input().split()))
p = o = 0
for i in a:
    if i > 0:
        p += 1
    elif i < 0:
        o += 1
if 2 * p >= n:
    print(1)
elif 2 * o >= n:
    print(-1)
else:
    print(0)

