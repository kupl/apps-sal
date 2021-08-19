n = int(input())
l = [i for i in input().split(' ')]
ma = 0
for i in l:
    c = 0
    for j in i:
        if j.isupper() == True:
            c += 1
    if c > ma:
        ma = c
print(ma)
