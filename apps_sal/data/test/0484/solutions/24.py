n, w, h = list(map(int, input().split()))


def chk(w1, h1, w2, h2):
    if w1 <= w and h1 <= h:
        if w - w1 >= w2 and h >= h2 or w - w1 >= h2 and h >= w2 or w >= w2 and h - h1 >= h2 or w >= h2 and h - h1 >= w2:
            return True
    if h1 <= w and w1 <= h:
        if w - h1 >= w2 and h >= h2 or w - h1 >= h2 and h >= w2 or w >= w2 and h - w1 >= h2 or w >= h2 and h - w1 >= w2:
            return True
    return False


a, ans = [], 0
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append([x, y])
for i in range(n):
    for j in range(i + 1, n):
        if a[i][0] * a[i][1] + a[j][1] * a[j][0] > ans and chk(a[i][0], a[i][1], a[j][0], a[j][1]):
            ans = a[i][0] * a[i][1] + a[j][1] * a[j][0]
print(ans)
