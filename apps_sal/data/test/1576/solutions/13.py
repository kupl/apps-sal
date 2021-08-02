s = input()
result = []
for i in reversed(range(len(s))):
    if i % 2 == 0:
        result.append(s[0])
        s = s[1:]
    else:
        result.append(s[-1])
        s = s[:-1]
result.reverse()
print(''.join(result))
