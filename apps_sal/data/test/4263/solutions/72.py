n = str(input())

pattern = 'ACGT'
r, tmp = 0, 0
c = False
for s in n:
    if s in pattern:
        tmp += 1
    else:
        if r < tmp:
            r = tmp
        tmp = 0
if r < tmp:
    r = tmp
print(r)
