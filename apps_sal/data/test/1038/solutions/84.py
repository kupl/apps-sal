a, b = list(map(int, input().split()))

# 2n と 2n+1 のxorは1になることを利用
if a % 2 == 0:
    ans = 0
    q, r = divmod(b - a + 1, 2)
else:
    ans = a
    q, r = divmod(b - a, 2)

if q & 1:
    ans ^= 1
else:
    ans ^= 0
if r:
    ans ^= b

print(ans)
