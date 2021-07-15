h, w = list(map(int, input().split()))


def calc(a, b):
    ret = a * b
    for i in range(1, a):
        area1 = b // 2 * i
        area2 = -(-b // 2) * i
        area3 = a * b - (area1 + area2)
        #print(area1, area2, area3)
        ret = min(ret, max(area1, area2, area3) - min(area1, area2, area3))
    return ret

if h % 3 == 0 or w % 3 == 0:
    print((0))
else:
    ans = h * w
    for i in range(1, max(h, w) - 1):
        area1 = min(h, w) * i
        area2 = min(h, w) * ((max(h, w) - i) // 2)
        area3 = min(h, w) * (-(-(max(h, w) - i) // 2))
        #print(area1, area2, area3)
        ans = min(ans, max(area1, area2, area3) - min(area1, area2, area3))
    print((min(calc(h, w), calc(w, h), ans)))

