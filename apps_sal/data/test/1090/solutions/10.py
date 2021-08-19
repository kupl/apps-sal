(n, k) = map(int, input().split())
s = input()
score = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        score += 1
ans = min(score + 2 * k, n - 1)
print(ans)
