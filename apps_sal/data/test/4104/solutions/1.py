s = input()
ops = []
for i in range(0, len(s)):
    ch = s[i]
    if ch == '+' or ch == '-':
        ops.append(i)
ops.append(len(s))
for i in range(0, len(ops) - 1):
    ch = s[ops[i]]
    if ch == '-':
        s += '+3'
    if ch == '+':
        s += '-5'
    for j in range(ops[i], ops[i + 1] - 1):
        s += '0'
print(eval(s))
