from bisect import bisect_left, bisect_right
n = int(input())
sh = sorted(list(input()))
mor = sorted(list(input()))
temp = []
get = 0
for elem in sh:
    a = bisect_left(mor, elem)
    if a >= len(mor):
        get += 1
        a = 0
    temp.append(mor[a])
    mor.pop(a)
mor = sorted(temp)
temp = []
give = 0
for elem in sh:
    a = bisect_right(mor, elem)
    if a < len(mor):
        give += 1
    else:
        a = 0
    mor.pop(a)
print(get, give, sep='\n')
