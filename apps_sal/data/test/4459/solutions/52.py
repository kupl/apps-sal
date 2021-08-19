n = int(input())
al = list(map(int, input().split()))
ans = 0
dic = {}
for a in al:
    dic[a] = dic.get(a, 0) + 1
for (k, v) in dic.items():
    if k == v:
        pass
    elif k < v:
        ans += v - k
    else:
        ans += v
print(ans)
