def resolve():
    H, W = list(map(int, input().split()))
    
    def _solve(H, W):
        mean_w = W // 2
        ans = float("inf")
        for h in range(1, H):
            s1 = h * W
            mean_h = (H-h) // 2
            for i in range(0, 2):
                if i == 0:
                    s2 = (H-h)*mean_w
                    s3 = (H-h)*(W-mean_w)
                if i == 1:
                    s2 = mean_h*W
                    s3 = (H-h-mean_h)*W
                ans = min(ans, max(s1, s2, s3)-min(s1, s2, s3))
        return ans

    print(min(_solve(H, W), _solve(W, H)))

if '__main__' == __name__:
    resolve()
