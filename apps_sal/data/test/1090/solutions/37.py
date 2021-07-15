n, k = list(map(int, input().split()))
s = input()
score = 0
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        score += 1

ans = min(n - 1, score + 2 * k)

print(ans)

