n = int(input())
li = list(map(int, input().split()))
s = [li[0]]
ans = 0
m = 10**9 + 7
for i in range(n - 1):
    s.append(li[i + 1] + s[i])

for j in range(n - 1):
    ans += (li[j] * (s[n - 1] - s[j])) % m

print(ans % m)
