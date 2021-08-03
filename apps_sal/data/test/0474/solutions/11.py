n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
c = 0
temp = 0
for x in arr:
    if x == m:
        c += 1
    else:
        if temp < c:
            temp = c
        c = 0
if temp < c:
    temp = c
print(temp)
