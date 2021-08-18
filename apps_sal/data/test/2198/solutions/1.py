import sys


fin = sys.stdin


[n, m] = [int(x) for x in fin.readline().split()]
s = [(x == '.') for x in fin.readline().rstrip()]


count = 0
for i in range(1, len(s)):
    if s[i] and s[i - 1]:
        count += 1

for i in range(m):
    [index, char] = fin.readline().split()
    index = int(index) - 1
    if s[index] and char != '.':
        if index > 0 and s[index - 1]:
            count -= 1
        if index < n - 1 and s[index + 1]:
            count -= 1
        s[index] = False
    elif (not s[index]) and char == '.':
        if index > 0 and s[index - 1]:
            count += 1
        if index < n - 1 and s[index + 1]:
            count += 1
        s[index] = True
    print(count)
