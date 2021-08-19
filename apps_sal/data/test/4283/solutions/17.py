n = int(input())
l = list(map(int, input().split()))
l.sort()
maxs = 1
min_el = l[0]
min_ind = 0
s = 1
for i in range(1, len(l)):
    if l[i] - min_el <= 5:
        s += 1
    else:
        min_el = l[min_ind + 1]
        min_ind = min_ind + 1
    maxs = max(maxs, s)
maxs = max(maxs, s)
print(maxs)
