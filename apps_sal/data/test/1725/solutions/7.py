def polo(l, d):
    l.sort()
    # find median k
    k = l[int(len(l) / 2)]
    s = 0

    # loop through again and calculate if each element |x-k| % d == 0
    # if so, add k to sum
    for n in l:
        if abs(n - k) % d == 0:
            s = s + abs(n - k)
        else:
            return -1
    return int(s / d)


l = []
n, m, d = [int(x) for x in input().split(' ')]
for _ in range(n):
    l.extend(int(x) for x in input().split(' '))

print(polo(l, d))
