s = input()
count = 0
for i in range(3):
    if s[i] == 'R':
        if count == 0:
            count += 1
        elif s[i - 1] == 'R':
            count += 1
print(count)
