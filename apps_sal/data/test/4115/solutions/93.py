s = input()
count = 0
for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        count += 1
print(count)
