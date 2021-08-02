a, b = [input() for i in range(2)]
p = 0
ans = 0

for i in b:
    if i == 'I':
        p += 1
    elif i == 'D' and p > 0:
        p -= 1
    else:
        p -= 1

    if ans < p:
        ans = p

print(ans)
