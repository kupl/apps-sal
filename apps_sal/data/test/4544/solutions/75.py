N = int(input())
a = list(map(int, input().split()))
count = [0 for _ in range(100001)]
for x in a:
    count[x] += 1
    count[x + 1] += 1
    if x > 0:
        count[x - 1] += 1
print(max(count))
