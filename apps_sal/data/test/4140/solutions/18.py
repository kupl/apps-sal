s = input()
result = 10 ** 9
tmp = 0
for (i, c) in enumerate(s):
    if i & 1:
        if c == '0':
            tmp += 1
    elif c == '1':
        tmp += 1
result = min(result, tmp)
tmp = 0
for (i, c) in enumerate(s):
    if i & 1:
        if c == '1':
            tmp += 1
    elif c == '0':
        tmp += 1
result = min(result, tmp)
print(result)
