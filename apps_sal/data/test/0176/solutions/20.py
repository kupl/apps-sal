(k, a, b) = map(int, input().split())
ans = 0
if a < 0 and b <= 0:
    (a, b) = (abs(b), abs(a))
if a > 0 and a % k:
    a = a + k - a % k
    if a <= b:
        ans += (b - a) // k + 1
elif a >= 0:
    ans += (b - a) // k + 1
elif a < 0 and abs(a) % k:
    a = abs(a) - abs(a) % k
    ans += a // k + 1
    ans += b // k
elif a < 0:
    ans += abs(a) // k + 1
    ans += b // k
print(ans)
