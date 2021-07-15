s = list(input())

while s[0] != 'A' or s[-1] != 'Z':
    if s[0] == 'A':
        s.pop()
    elif s[-1] == 'Z':
        s.pop(0)
    else:
        s.pop(0)
        s.pop()

print(len(s))
