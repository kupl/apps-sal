n, k = map(int, input().split())
const = ''
ans = ''
for i in range(k):
    const += chr(i + 97)
ans = (n // k) * const
ans += const[:n % k]
print(ans)
