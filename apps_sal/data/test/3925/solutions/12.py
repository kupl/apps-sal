s = input()
last = s[0]
count = 1
best = 1
for i in range(1, len(s) * 2):
    if last != s[i % len(s)]:
        count += 1
        best = max(best, count)
        last = s[i % len(s)]
    else:
        count = 1
print(min(best, len(s)))
