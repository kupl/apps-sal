n = int(input())
a = list(map(int, input().split()))

s1, s3 = 0, 0
max_s = 0
l, r = 0, n-1
while l <= r:
    if s1 > s3:
        s3 += a[r]
        r -= 1
    else:
        s1 += a[l]
        l += 1

    if s1 == s3:
        max_s = s1

print(max_s)
