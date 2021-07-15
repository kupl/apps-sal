n, d, h = list(map(int, input().split()))

if (d-h > h) or (h == 1 and n >= 4 and d != 2) or (h == 1 and n == 3 and d == 1):
    print(-1)
    return

c = 1
for i in range(h):
    print(c, c+1)
    c += 1

if (c < n and d-h != 0):
    print(1, c+1)
    c += 1

for i in range(d-h-1):
    print(c, c+1)
    c += 1

while (c < n):
    if h == 1 and (d-h != 0):
        print(1, c+1)
    else:
        print(2, c+1)
    c += 1

