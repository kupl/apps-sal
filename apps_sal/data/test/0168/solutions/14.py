n = int(input())
l = input()
s = 0
for c in l:
    if c == '+':
        s += 1
    else:
        s -= 1
        if s < 0:
            s = 0

print(s)
