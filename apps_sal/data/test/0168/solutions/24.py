n = int(input())
ops = input()
c = 0
for o in ops:
    if o == '-':
        c = c - 1 if c > 0 else 0
    else:
        c += 1
print(c)
