n = int(input())
minutesUsed = [0 for _ in range(n)]

count = 1
for v in [int(k) for k in input().split(' ') if k]:
    if minutesUsed[v]:
        count += 1
    else:
        minutesUsed[v] = 1
print(count)

