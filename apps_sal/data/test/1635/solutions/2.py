n = int(input())
a = set()
res = 0
for i in list(map(int, input().split()))[::-1]:
    if i not in a:
        a.add(i)
        res = i
print(res)

