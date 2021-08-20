import sys
input = sys.stdin.readline
(H, W) = list(map(int, input().split()))
S = H * W
s1 = 0
ans = 10 ** 10
for i in range(1, H):
    s1 += W
    s2 = (H - i) * (W // 2)
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    s2 = (H - i) // 2 * W
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
s1 = 0
for i in range(1, W):
    s1 += H
    s2 = (W - i) * (H // 2)
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    s2 = (W - i) // 2 * H
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
print(ans)
