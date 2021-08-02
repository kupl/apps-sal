n = int(input())
cnt = [[0] * n for i in range(26)]

for i in range(n):
    s = input()
    for j in range(len(s)):
        x = ord(s[j]) - 97
        cnt[x][i] += 1

ans = ''
for i in range(26):
    ans += min(cnt[i]) * chr(i + 97)
print(ans)
