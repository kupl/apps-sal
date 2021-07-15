s = list(input())
count = 0
for i in range(0, len(s)):
    if s[i] == '+':
        count += 1
    elif s[i] == '-':
        count -= 1
print(count)
