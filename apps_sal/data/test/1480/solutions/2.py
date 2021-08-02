n, k = map(int, input().split())
data = map(int, input().split())
arr = [i + 1 for i in range(n)]
for v in data:
    l = len(arr)
    i = v % l
    print(arr[i], end=" ")
    arr = [arr[(i + k) % l] for k in range(1, l)]
print()
