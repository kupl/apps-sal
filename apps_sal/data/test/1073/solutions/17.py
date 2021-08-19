n = int(input())
s = input().rstrip()
count = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        (x, y) = (0, 0)
        for c in s[i:j + 1]:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x += 1
            elif c == 'R':
                x -= 1
        if x == 0 and y == 0:
            count += 1
print(count)
