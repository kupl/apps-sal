S = input()
res = [0] * len(S)
childlen = 0
for i in range(len(S)):
    if S[i] == 'R':
        childlen += 1
    else:
        tmp = (childlen + int(childlen % 2 == 1)) // 2
        res[i - 1] += tmp
        res[i] += childlen - tmp
        childlen = 0
for i in reversed(range(len(S))):
    if S[i] == 'L':
        childlen += 1
    else:
        tmp = (childlen + int(childlen % 2 == 1)) // 2
        res[i + 1] += tmp
        res[i] += childlen - tmp
        childlen = 0
print(*res)
