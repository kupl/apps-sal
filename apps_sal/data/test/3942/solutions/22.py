s = input()
ret = [None] * len(s)
bal = [None] * len(s)
b = 0
last = None
for i, c in enumerate(s):
    if c == '(':
        b += 1
    elif c == ')':
        b -= 1
    else:
        ret[i] = 1
        b -= 1
        last = i
    if b < 0:
        print(-1)
        return
    bal[i] = b
rem = bal[-1]
ret[last] += rem
for i in range(last, len(bal)):
    bal[i] -= rem
print('\n'.join(map(str, filter(lambda x: x, ret))) if min(bal) >= 0 else -1)
