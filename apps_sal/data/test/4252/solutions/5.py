n = int(input())
s = input() + '

res = 0
p = 0
for i, c in enumerate(s):
    if c == 'x':
        p += 1
    else:
        res += max(0, p - 2)
        p = 0

print(res)
