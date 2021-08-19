(n, m) = map(int, input().split())
dic = {}
ans = 0
for _ in range(n):
    lis = input().split()
    for i in range(1, len(lis)):
        if lis[i] in dic:
            dic[lis[i]] += 1
        else:
            dic[lis[i]] = 1
for v in dic.values():
    if v == n:
        ans += 1
print(ans)
