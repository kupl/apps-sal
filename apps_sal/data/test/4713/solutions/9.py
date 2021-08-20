n = int(input())
s = input()
res = x = 0
for s_ in s:
    if s_ == 'I':
        x += 1
    else:
        x -= 1
    res = max(res, x)
print(res)
