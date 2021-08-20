_ = int(input())
s = input()
chars = set()
maxval = 0
for c in s:
    if c.isupper():
        maxval = max(maxval, len(chars))
        chars = set()
    else:
        chars.add(c)
maxval = max(maxval, len(chars))
print(maxval)
