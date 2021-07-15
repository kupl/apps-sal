n, t = list(map(int, input().split()))
tlist = [int(t) for t in input().split()]
maxcount = 0
time = 0
i = 0
j = 0
count = 1
while j != n:
    if time + tlist[j] <= t:
        time += tlist[j]
        if maxcount < count:
            maxcount = count
        j += 1
        count += 1
    else:
        time -= tlist[i]
        i += 1
        count -= 1

print(maxcount)

# Время прохода - 2n

