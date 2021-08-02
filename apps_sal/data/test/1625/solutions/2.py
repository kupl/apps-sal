n = int(input())
arr = list(map(float, input().split()))
arr.sort(reverse=True)
res = 0
while arr:
    res += sum(arr)
    arr = arr[:len(arr) // 4]
print(int(res))
