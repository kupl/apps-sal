N = int(input())
ls = list(map(int, input().split(' ')))
ls.sort()
val = ls[0]
if N >= 2:
    for i in ls[1:]:
        val = (val + i) / 2
print(val)
