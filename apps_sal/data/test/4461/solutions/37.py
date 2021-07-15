h, w = map(int, input().split())
if h % 3 == 0 or w % 3 == 0:
    print(0)
else:
    ans = min(w, h)
    for w1 in range(w//3, w//3+3):
        s1 = w1 * h
        w2 = w-w1
        for h1 in range(h//2, h//2+2):
            s2 = w2 * h1
            s3 = w2 * (h-h1)
            ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    h, w = w, h
    for w1 in range(w//3, w//3+3):
        s1 = w1 * h
        w2 = w-w1
        for h1 in range(h//2, h//2+2):
            s2 = w2 * h1
            s3 = w2 * (h-h1)
            ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    print(ans)
