s = input()

result = 10 ** 9
# 0始まりで揃える場合
tmp = 0
for i, c in enumerate(s):
    if i & 1:
        if c == '0':
            tmp += 1
    else:
        if c == '1':
            tmp += 1

result = min(result, tmp)
tmp = 0

# 1始まりで揃える場合
for i, c in enumerate(s):
    if i & 1:
        if c == '1':
            tmp += 1
    else:
        if c == '0':
            tmp += 1

result = min(result, tmp)
print(result)
