(h, w) = list(map(int, input().split()))
tanpen = min(h, w)
chohen = max(h, w)
if h % 3 == 0 or w % 3 == 0:
    print(0)
else:

    def findmin(h, w):
        ans = h * w
        for i in range(1, h):
            remi = h - i
            s1 = i * w
            s2 = w // 2 * remi
            s3 = (w - w // 2) * remi
            ans = min(ans, max(s1, s2, s3) - min(s1, s2))
            s2 = w * (remi // 2)
            s3 = w * (remi - remi // 2)
            ans = min(ans, max(s1, s2, s3) - min(s1, s2))
        return ans
    print(min(findmin(h, w), findmin(w, h)))
