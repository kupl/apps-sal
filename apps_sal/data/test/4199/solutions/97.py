(n, k) = map(int, input().split())
heights = list(map(int, input().split()))
count = 0
for height in heights:
    if k <= height:
        count = count + 1
print(count)
