n = int(input())
dic = {}
ans = s = 0
k = input().split()
for i in range(n):
    a = int(k[i])

    if (a - 1) in dic:
        b = dic[a - 1]
    else:
        b = 0

    if a in dic:
        c = dic[a]
    else:
        c = 0
        dic.update({a: 0})

    if (a + 1) in dic:
        d = dic[a + 1]
    else:
        d = 0

    ans += a * (i - b - c - d) - s + b * (a - 1) + c * (a) + d * (a + 1)
    dic[a] += 1
    s += a

print(ans)
