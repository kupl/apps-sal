(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = [0 for i in range(101)]
for i in a:
    b[i] += 1
x = max(b)
if x % k != 0:
    x //= k
    x += 1
    x *= k
ans = 0
for i in range(101):
    if b[i] != 0:
        ans += x - b[i]
print(ans)
