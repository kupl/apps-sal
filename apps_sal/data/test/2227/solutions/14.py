
subst = input().split('heavy')

res = 0
for i in range(len(subst)):
    res += i * subst[i].count('metal')

print(res)

