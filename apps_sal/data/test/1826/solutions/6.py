def check(s):
    for i in range(len(s) - 1):
        if s[i] == 'R' and s[i + 1] == 'U' or s[i] == 'U' and s[i + 1] == 'R':
            return i
    return -1


n = int(input())
s = input()
x = 0
for i in range(100):
    a = check(s)
    if a != -1:
        s = s[:a] + 'D' + s[a + 2:]
        x += 1
print(len(s))
