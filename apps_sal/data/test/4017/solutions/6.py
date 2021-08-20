n = int(input())
l = list(map(int, input().split()))
s = sum(l)
(max1, max2) = sorted(l, reverse=True)[:2]
pretty_indexes = []
for (i, ll) in enumerate(l, start=1):
    if s - ll == 2 * (max1 if ll != max1 else max2):
        pretty_indexes.append(str(i))
print(len(pretty_indexes))
print(' '.join(pretty_indexes))
