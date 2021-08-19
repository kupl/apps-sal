from copy import copy
n = int(input())
a = input()
s = list(a)
ans = copy(s)
left = 0
right = 0
for i in range(n):
    if s[i] == '(':
        left += 1
    elif left == 0:
        right += 1
    else:
        left -= 1
print('(' * right + str(a) + ')' * left)
