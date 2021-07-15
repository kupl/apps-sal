a = set()
n = int(input())
k = list(map(int, input().split()))
res = 0
for i in range (len(k)):
    if (k[i] in a):
        a.remove(k[i])
    else:
        a.add(k[i])
    res = max(res, len(a))
print(res)
