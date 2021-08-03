n = int(input())
small = []
large = []
idx = {}
for i in range(1, n + 1):
    tup = input().split()
    tup[0] = int(tup[0])
    tup[1] = int(tup[1])
    tup = tuple(tup)
    idx[tup] = i
    if tup[0] > tup[1]:
        large.append(tup)
    else:
        small.append(tup)
small_best = False
if len(small) > len(large):
    small_best = True
    small.sort(reverse=True)
else:
    large.sort()
if small_best == True:
    print(len(small))
    for tup in small:
        print(idx[tup], end=" ")
    print()
else:
    print(len(large))
    for tup in large:
        print(idx[tup], end=" ")
    print()
