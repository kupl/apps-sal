h, w, n = [int(i) for i in input().split()]
A = [0 for _ in range(n)]
B = [0 for _ in range(n)]
cnt = {}


for i in range(n):
    a, b = [int(j) for j in input().split()]
    if a > 1 and b > 1 and a < h and b < w:
        if "{} {}".format(a, b) not in list(cnt.keys()):
            cnt["{} {}".format(a, b)] = 0
        cnt["{} {}".format(a, b)] += 1
    if a > 2 and b > 2 and a <= h and b <= w:
        if "{} {}".format(a - 1, b - 1) not in list(cnt.keys()):
            cnt["{} {}".format(a - 1, b - 1)] = 0
        cnt["{} {}".format(a - 1, b - 1)] += 1
    if a > 2 and b > 1 and a <= h and b < w:
        if "{} {}".format(a - 1, b) not in list(cnt.keys()):
            cnt["{} {}".format(a - 1, b)] = 0
        cnt["{} {}".format(a - 1, b)] += 1
    if a > 2 and b > 0 and a <= h and b < w - 1:
        if "{} {}".format(a - 1, b + 1) not in list(cnt.keys()):
            cnt["{} {}".format(a - 1, b + 1)] = 0
        cnt["{} {}".format(a - 1, b + 1)] += 1
    if a > 1 and b > 2 and a < h and b <= w:
        if "{} {}".format(a, b - 1) not in list(cnt.keys()):
            cnt["{} {}".format(a, b - 1)] = 0
        cnt["{} {}".format(a, b - 1)] += 1
    if a > 0 and b > 0 and a < h - 1 and b < w - 1:
        if "{} {}".format(a + 1, b + 1) not in list(cnt.keys()):
            cnt["{} {}".format(a + 1, b + 1)] = 0
        cnt["{} {}".format(a + 1, b + 1)] += 1
    if a > 0 and b > 1 and a < h - 1 and b < w:
        if "{} {}".format(a + 1, b) not in list(cnt.keys()):
            cnt["{} {}".format(a + 1, b)] = 0
        cnt["{} {}".format(a + 1, b)] += 1
    if a > 1 and b > 0 and a < h and b < w - 1:
        if "{} {}".format(a, b + 1) not in list(cnt.keys()):
            cnt["{} {}".format(a, b + 1)] = 0
        cnt["{} {}".format(a, b + 1)] += 1
    if a > 0 and b > 2 and a < h - 1 and b <= w:
        if "{} {}".format(a + 1, b - 1) not in list(cnt.keys()):
            cnt["{} {}".format(a + 1, b - 1)] = 0
        cnt["{} {}".format(a + 1, b - 1)] += 1

count = [0 for i in range(10)]
for i in list(cnt.values()):
    count[i] += 1
count[0] = (h - 2) * (w - 2) - len(cnt)

for i in count:
    print(i)
