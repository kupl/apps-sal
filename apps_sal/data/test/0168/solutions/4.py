n = int(input())
x = input()
cur = 0
for c in x:
    if c == '-':
        while cur <= 0:
            cur += 1
        cur -= 1
    else:
        cur += 1
print(cur)
