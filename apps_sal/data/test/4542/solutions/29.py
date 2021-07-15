prev = '0'
S = ''
for c in input():
    if c != prev:
        S += c
    prev = c
print(len(S) - 1)
