n = int(input())
s = input()
xc = 0
res = 0
for i in s:
    if i == 'x':
        xc += 1
    else:
        if xc >= 3:
            res += xc - 2
        xc = 0
if xc >= 3:
    res += xc - 2
print(res)
