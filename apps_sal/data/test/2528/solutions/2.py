n = int(input())
arr = [int(x) for x in input().split()]
subarr = []
prev = []
if 0 in arr:
    for val in range(len(arr)):
        if arr[val] == 0:
            if len(subarr) > len(prev):
                prev = subarr
            subarr = []

        else:
            subarr.append(arr[val])
    print(max(len(prev), len(subarr)))
else:
    print(n)
