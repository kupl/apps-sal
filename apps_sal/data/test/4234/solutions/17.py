n = int(input())
s = input()
count = 0
good = ''
i = 0
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        count += 1
        i += 1
    else:
        good += s[i:i + 2]
        i += 2
if i == len(s) - 1:
    count += 1
print(count)
print(good)
