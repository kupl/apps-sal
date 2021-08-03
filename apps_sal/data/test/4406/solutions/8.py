n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

nowlist = []
nowset = set()

for i in arr:
    if i in nowset:
        continue
    if len(nowlist) == k:
        nowset.remove(nowlist.pop())
    nowlist = [i] + nowlist
    nowset.add(i)

print(len(nowlist))
print(*nowlist)
