s = input()

b = [0] * len(s)

ob = 0
cc = 0
p = -1
q = -1

count = 0

for ind, c in enumerate(s):
    if c == '[':
        ob = 1
    elif c == ':' and p >= 0:
        q = ind
    elif c == ':' and ob == 1 and p < 0:
        p = ind
    elif c == ']' and q >= 0:
        cc = q
    elif c == '|':
        count += 1
    b[ind] = count

if cc > 0:
    print(4 + b[cc] - b[p])
else:
    print(-1)
