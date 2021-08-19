(a, b) = map(int, input().split())
ans = ''
for i in range(-1 * 10 ** 6, 10 ** 6):
    if b - a + 1 <= i <= b + a - 1:
        ans += str(i) + ' '
print(ans[:-1])
