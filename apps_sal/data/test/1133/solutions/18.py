n = int(input())
s = [input() for i in range(n)]
l = [(set(x), len(x)) for x in s if len(set(x)) < 3]
ans = 0
n = len(l)
t = [''] + list('qwertyuiopasdfghjklzxcvbnm')
for i in range(27):
    for j in range(27):
        if i == j:
            continue
        r = 0
        for k in range(n):
            if len(l[k][0] | {t[i]} | {t[j]}) < 3:
                r += l[k][1]
        if r > ans:
            ans = r
print(ans)
