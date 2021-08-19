# Take your protein pills and put your helmet on...
n, m, k = map(int, input().split())
d = {}
arr = [int(x) for x in input().split()]
sch = [int(x) for x in input().split()]
for i in range(len(arr)):
    d[sch[i]] = max(d.get(sch[i], 0), arr[i])
select = [int(x) for x in input().split()]
cnt = 0
for i in select:
    if d[sch[i - 1]] != arr[i - 1]:
        cnt += 1
print(cnt)
