n = int(input())
s = input()
ans = 0
for i in range(n):
    for t in range(i + 1):
        s1 = s[t:i + 1]
        x = 0
        y = 0
        for e in range(len(s1)):
            if s1[e] == 'U':
                y += 1
            elif s1[e] == 'R':
                x += 1
            elif s1[e] == 'D':
                y -= 1
            else:
                x -= 1
        if x == y == 0:
            ans += 1
print(ans)
