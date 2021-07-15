s = list(map(int, input()))
cnt = 0

for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        s[i + 1] = abs(s[i + 1] * 1 - 1)
        cnt += 1
print(cnt)
