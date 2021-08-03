n = int(input())
lst = list(map(int, input().split()))
lst.sort()
dayCount = 0
for i in lst:
    if i >= dayCount + 1:
        dayCount += 1
print(dayCount)
