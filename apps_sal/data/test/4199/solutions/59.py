(n, h) = map(int, input().split())
shin = list(map(int, input().split()))
count = 0
for i in shin:
    if i >= h:
        count += 1
print(count)
