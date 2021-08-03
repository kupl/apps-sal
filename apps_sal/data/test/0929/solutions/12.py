h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
th, tw = 0, 0
mode = 0
ans = []
ope = 0
while ope < h * w:
    if mode == 0:
        if tw == w - 1:
            if a[th][tw] % 2 == 1 and th + 1 < h:
                a[th][tw] -= 1
                a[th + 1][tw] += 1
                ans.append([th + 1, tw + 1, th + 2, tw + 1])
            th += 1
            mode = 1
        else:
            if a[th][tw] % 2 == 1:
                a[th][tw] -= 1
                a[th][tw + 1] += 1
                ans.append([th + 1, tw + 1, th + 1, tw + 2])
            tw += 1
    elif mode == 1:
        if tw == 0:
            if a[th][tw] % 2 == 1 and th + 1 < h:
                a[th][tw] -= 1
                a[th + 1][tw] += 1
                ans.append([th + 1, tw + 1, th + 2, tw + 1])
            th += 1
            mode = 0
        else:
            if a[th][tw] % 2 == 1:
                a[th][tw] -= 1
                a[th][tw - 1] += 1
                ans.append([th + 1, tw + 1, th + 1, tw])
            tw -= 1
    ope += 1
# print(a)
print((len(ans)))
for aa in ans:
    print((*aa))
