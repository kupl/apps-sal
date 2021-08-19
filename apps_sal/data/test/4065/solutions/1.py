n = int(input())
s = input().split()
for i in range(n):
    s[i] = int(s[i])
ans = 1
curStreak = 1
for i in range(1, n):
    if s[i] <= 2 * s[i - 1]:
        curStreak += 1
        ans = max(ans, curStreak)
    else:
        curStreak = 1
print(ans)
