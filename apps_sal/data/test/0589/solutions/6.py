s = input()
letters = set()
answer = 1
for ch in s:
    if ch == '?':
        answer *= 10
    elif ch >= 'A':
        letters.add(ord(ch))
temp = 10
for i in range(len(letters)):
    answer *= temp
    temp -= 1
if s[0] == '?' or s[0] >= 'A':
    answer = answer // 10 * 9
print(answer)
