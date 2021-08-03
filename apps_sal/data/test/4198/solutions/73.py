A, B, X = list(map(int, input().split()))

l = 0
r = 10**9
while r - l > 1:
    c = (r + l) // 2
    if X >= A * c + B * len(str(c)):
        l = c
    else:
        r = c
ans = l

m = 10**9
if X >= A * m + B * 10:
    ans = m

print(ans)
