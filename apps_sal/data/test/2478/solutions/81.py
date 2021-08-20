n = int(input())
s = input()
cntr = 0
for i in range(n - 1, -1, -1):
    if s[i] == ')':
        cntr += 1
    elif cntr > 0:
        cntr -= 1
s = '(' * cntr + s
n = len(s)
cntl = 0
for i in range(n):
    if s[i] == '(':
        cntl += 1
    elif cntl > 0:
        cntl -= 1
s += ')' * cntl
print(s)
