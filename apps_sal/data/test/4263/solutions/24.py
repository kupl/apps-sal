s = input()
count = 0
max = 0
for i in range(0, len(s)):
    if s[i] == 'A' or s[i] == 'T' or s[i] == 'G' or s[i] == 'C':
        count += 1
        if max < count:
            max = count
    else: count = 0
print(max)
