n = int(input())
lst = []
for i in range(n):
    ai, bi = list(map(int, input().split()))
    lst.append([ai, bi])
lst.sort()
path = []
last = 0
for i in lst:
    if min(i) >= last:
        path.append(min(i))
        last = min(i)
    else:
        path.append(max(i))
        last = max(i)
print(path[-1])
