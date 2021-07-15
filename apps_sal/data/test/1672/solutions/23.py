n = int(input())
s = []
x = 1
s.append('09')
for i in range(1, n + 1):
    s.append(input())
    if s[i - 1][1] == s[i][0]:
        x += 1
print(x)
