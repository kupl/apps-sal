n, k = [int(x) for x in input().split()]
xs = [int(x) for x in input().split()]

count = 1
cur_s = 0

for i in range(n - 1):
    next_dist = xs[i + 1] - xs[i]
    if next_dist > k:
        count = -1
        break
    elif next_dist + cur_s > k:
        cur_s = next_dist
        count += 1
    else:
        cur_s += next_dist

print(count)



