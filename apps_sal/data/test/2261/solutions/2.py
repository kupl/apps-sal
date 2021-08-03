def anti(s):
    return "".join(['+' if s[i] == '*' else '*' for i in range(len(s))])


k = int(input())
result = [[] for i in range(k + 2)]
result[0] = ['+']
for i in range(1, k + 1):
    for e in result[i - 1]:
        result[i] += [e + e]
        result[i] += [e + anti(e)]

print("\n".join(result[k]))
