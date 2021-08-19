n = int(input())
l = [int(x) for x in input().split()]
c = 0
ci = 0
for i in l:
    if i != 0:
        c += 1
        if c > ci:
            ci = c
    else:
        c = 0
print(ci)
