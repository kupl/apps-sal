n = int(input())

l = []
r = []

for i in range(n):
    numbers_in_line = [int(num) for num in input().split()]
    l_new, r_new = numbers_in_line
    l.append(l_new)
    r.append(r_new)

l.sort()
r.sort()

maxes = [max(lv, rv) for lv, rv in zip(l, r)]

print(n + sum(maxes))
