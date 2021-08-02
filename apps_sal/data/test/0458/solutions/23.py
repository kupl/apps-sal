def sumofdigits(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans


a, b, c = map(int, input().split())
ans = []
for s in range(1, 82):
    d = b * s**a + c
    if sumofdigits(d) == s and 0 < d < 1000000000:
        ans.append(d)
print(len(ans), '\n', ' '.join(map(str, ans)), sep='')
