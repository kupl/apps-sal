n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

max_sum = 0

for i in range(m):
    l, r = [int(x) for x in input().split()]
    l -= 1

    sucet = sum(a[l:r])

    if sucet > 0:
        max_sum += sucet

print(max_sum)
