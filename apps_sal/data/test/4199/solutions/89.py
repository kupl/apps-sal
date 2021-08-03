n, k = map(int, input().split())
xlist = list(map(int, input().split()))
count = 0
for i in range(n):
    if xlist[i] >= k:
        count += 1
print(count)
