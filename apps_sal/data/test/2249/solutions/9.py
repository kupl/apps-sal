n = int(input())
a = list(map(int, input().split()))

dic = {}
for i in range(len(a) - 1):
    if a[i] not in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1

been = set([])
cnt = 0
for i in range(len(a) - 1, 0, -1):
    if a[i] not in been:
        cnt += len(dic)
        been.add(a[i])
    dic[a[i - 1]] -= 1
    if (dic[a[i - 1]] == 0):
        del dic[a[i - 1]]
print(cnt)

