# Codeforces 265 Div. 2
# A

n = int(input())
l = list(input())
c = 0

for x in l:
    if int(x) == 0:
        c += 1
        break
    else:
        c += 1

print(c)
