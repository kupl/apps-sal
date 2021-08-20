n = int(input())
plist = list(map(int, input().split()))
tmpmin = 2 * 10 ** 5
count = 0
for i in range(n):
    if tmpmin >= plist[i]:
        tmpmin = plist[i]
        count += 1
print(count)
