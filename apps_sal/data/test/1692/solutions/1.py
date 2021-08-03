lst = input().strip()
s = []
for i in range(len(lst)):
    s.append(int(lst[i]))
answer = 0
for i in range(1, len(s)):
    if (s[i] + 10 * s[i - 1]) % 4 == 0:
        answer += i
for i in range(len(s)):
    if s[i] % 4 == 0:
        answer += 1
print(answer)
