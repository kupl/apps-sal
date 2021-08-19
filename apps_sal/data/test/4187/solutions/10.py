n = int(input())
a = [int(t) for t in input().split(' ')]
a.extend(a)
max_ones = 0
ones = 0
for ai in a:
    if ai == 1:
        ones += 1
    else:
        max_ones = max(max_ones, ones)
        ones = 0
print(max_ones)
