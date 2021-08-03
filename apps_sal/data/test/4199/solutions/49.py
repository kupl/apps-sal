n, k = list(map(int, input().split()))
friend = list(map(int, input().split()))

count = 0
for x in friend:
    if x >= k:
        count += 1

print(count)
