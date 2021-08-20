(n, k) = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
ids = [int(x) - 1 for x in input().split()]
s = sum(c)
ans = 0
for i in range(n):
    ans += c[i] * c[(i + 1) % n]
for i in range(k):
    if abs(ids[i] - ids[(i + 1) % k]) == 1 or (ids[i] == n - 1 and ids[0] == 0):
        ans += c[ids[i]] * c[ids[(i + 1) % k]]
temp = 0
for i in range(k):
    ans += c[ids[i]] * (s - c[(ids[i] - 1) % n] - c[(ids[i] + 1) % n] - c[ids[i]])
    ans -= c[ids[i]] * temp
    temp += c[ids[i]]
print(repr(ans))
