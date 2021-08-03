n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    dic.setdefault(a[i], 0)
    dic[a[i]] += 1
ans = []
for item in list(dic.items()):
    if item[1] >= 2:
        ans.append(item[0])
if len(ans) <= 1:
    print((0))
else:
    ans.sort()
    if dic[ans[-1]] >= 4:
        print((ans[-1]**2))
    else:
        print((ans[-1] * ans[-2]))
