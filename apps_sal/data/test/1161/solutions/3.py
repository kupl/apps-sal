import math
s = input().rstrip()
n = len(s)
stack = []
k = 0
D = {'(': 0, '{': 2, '[': 4, '<': 6, ')': 1, '}': 3, ']': 5, '>': 7}
for i in range(n):
    c = s[i]
    if D[c] % 2 == 0:
        stack.append(c)
    elif len(stack) == 0 or D[stack[-1]] % 2:
        print('Impossible')
        break
    else:
        k += D[c] - D[stack[-1]] != 1
        stack.pop()
else:
    print(k if len(stack) == 0 else 'Impossible')
