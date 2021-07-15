arr = list(map(int, input().split('+')))
arr.sort()
for i in arr[:-1]:
    print(str(i), end='+')
print(arr[-1])
