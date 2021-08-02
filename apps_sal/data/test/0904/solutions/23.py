input()
l = [i for i in input().split()]
ans = 0
for i in l:
    d = 0
    for j in i:
        if j.isupper():
            d += 1
    ans = max(ans, d)
print(ans)
