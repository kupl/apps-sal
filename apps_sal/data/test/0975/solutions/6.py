import collections

n = int(input())
sh = input()
mor = input()

sh_dig = collections.Counter(sh)
mor_dig = collections.Counter(mor)

sh_sort = sorted(sh)
mor_sort = sorted(mor)

min_strikes = 0
i, j = 0, 0
while j != n:
    if sh_sort[i] <= mor_sort[j]:
        i += 1
        j += 1
    else:
        min_strikes += 1
        j += 1

max_strikes = 0
i, j = 0, 0
while j != n:
    if sh_sort[i] < mor_sort[j]:
        max_strikes += 1
        i += 1
        j += 1
    else:
        j += 1

print(min_strikes)
print(max_strikes)
