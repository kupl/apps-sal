(n, k) = list(map(int, input().split()))
num = [0] * k
for i in range(1, n + 1):
    num[i % k] += 1
ans = 0
for a in range(k):
    b = (k - a) % k
    c = (k - a) % k
    if (b + c) % k != 0:
        continue
    ans += num[a] * num[b] * num[c]
print(ans)
