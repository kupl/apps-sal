n = int(input())
e = input().split(' ')
best = 0
for i in e:
    loc = 0
    for j in i:
        if j.isupper():
            loc += 1
    best = max(best, loc)

print(best)
