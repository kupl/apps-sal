(n, k) = [int(item) for item in input().split()]
a = sorted([int(item) for item in input().split()], reverse=True)
count = 0
asum = 0
for item in a:
    if asum + item < k:
        asum += item
        count += 1
    else:
        count = 0
print(count)
