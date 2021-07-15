n, m = map(int, input().split())
div = n // m
mod = n % m
lst = []
k = 1
for i in range(m):
    lst.append(div)
for item in lst:
    if mod != 0 and mod > 0:
        lst[lst.index(item)] = lst[lst.index(item)] + 1
    mod = mod - 1
lst.sort()
for item in lst:
    if k == len(lst)-1:
        print(item)
    print(item, end = ' ')
    

