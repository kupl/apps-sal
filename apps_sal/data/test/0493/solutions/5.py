n = int(input())
s = input()
r = [0] * n
l = [0] * n
index = -1
for i in range(0, n):
    if s[i] == '.':
        r[i] = index
    elif s[i] == 'R':
        index = i
        r[i] = 0
    elif s[i] == 'L':
        r[i] = -1
        index = -1
index = -1
result = 0
for i in range(n - 1, -1, -1):
    if s[i] == '.':
        l[i] = index
    elif s[i] == 'L':
        index = i
        l[i] = 0
    elif s[i] == 'R':
        l[i] = -1
        index = -1
    if (l[i] < 0 and r[i] < 0) or (l[i] >= 0 and r[i] >= 0 and l[i] - i == i - r[i]):
        result += 1
print(result)
