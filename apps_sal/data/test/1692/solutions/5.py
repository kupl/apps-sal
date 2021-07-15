s = input()
cnt = 0
for i in range(1, len(s)):
    if int(s[i - 1] + s[i]) % 4 == 0:
        cnt += i
cnt += sum(int(i) % 4 == 0 for i in s)
print(cnt)

