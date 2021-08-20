(h1, h2) = list(map(int, input().split(' ')))
(a, b) = list(map(int, input().split(' ')))
if h1 + 8 * a >= h2:
    print(0)
elif a <= b:
    print(-1)
else:
    cnt = 0
    h1 += 8 * a
    while h1 < h2:
        h1 += 12 * (a - b)
        cnt += 1
    print(cnt)
