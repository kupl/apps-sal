n = int(input())
data = list(map(int, input().split()))
lst = dict()
tme = dict()
for i in range(n):
    if data[i] in list(lst.keys()):
        lst[data[i]] += 1
    else:
        lst[data[i]] = 1
    tme[data[i]] = i
ps = -1
mx = -1
time = -1
for i in list(lst.keys()):
    if lst[i] > mx:
        mx = lst[i]
        time = tme[i]
        ps = i
    elif lst[i] == mx:
        if time > tme[i]:
            time = tme[i]
            ps = i
print(ps)
