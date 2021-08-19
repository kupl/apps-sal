s = input()
piece = ''
count = 0
for i in range(len(s) - 1):
    if s[i + 1] != s[i]:
        piece += s[i]
        if len(piece) % 2 == 0:
            count += 1
        piece = ''
    else:
        piece += s[i]
        if i == len(s) - 2 and s[len(s) - 2] == s[len(s) - 1]:
            piece += s[-1]
            if len(piece) % 2 == 0:
                count += 1
print(count)
