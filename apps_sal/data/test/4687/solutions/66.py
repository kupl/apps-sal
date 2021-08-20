(n, k) = list(map(int, input().split()))
dic = {}
for i in range(n):
    (a, b) = list(map(int, input().split()))
    dic[a] = dic.get(a, 0) + b
l = sorted(dic.items())
for (a, b) in l:
    if k <= b:
        ans = a
        break
    k -= b
print(ans)
