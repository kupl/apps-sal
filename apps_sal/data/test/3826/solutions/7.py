n = int(input())

a = list(map(int, input().split()))
min1 = n + 1
myset = set()
for i in range(n):
    temp = myset.copy()
    min1 = min(min1, n - i)
    for j in range(n - 1, i - 1, -1):
        if(a[j] in temp):
            break
        temp.add(a[j])
        min1 = min(min1, j - i)
    if(a[i] in myset):
        break
    myset.add(a[i])
    # print(myset, min1)

print(min1)
