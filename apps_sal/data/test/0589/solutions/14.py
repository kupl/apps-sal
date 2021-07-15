hint = input()
seen = []

if 'A' <= hint[0] <= 'J':
    num = 9
    seen = [hint[0]]
elif '0' <= hint[0] <= '9':
    num = 1
elif hint[0] == '?':
    num = 9

for l in hint[1:]:
    if 'A' <= l <= 'J':
        if not l in seen:
            num *= 10 - len(seen)
            seen += [l]
    elif l == '?':
        num *= 10

print(num)

