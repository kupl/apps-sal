n = int(input())
s = input()
countr, countl = 0, 0

for i in range(n - 1, -1, -1):
    if s[i] == ')':
        countr += 1
    elif countr > 0:
        countr -= 1
s = '(' * countr + s
n = len(s)

for i in range(n):
    if s[i] == '(':
        countl += 1
    elif countl > 0:
        countl -= 1
s += ')' * countl

print(s)
