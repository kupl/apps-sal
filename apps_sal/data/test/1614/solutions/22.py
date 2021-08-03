n, h = map(int, input().split())
arr = list(map(int, input().split()))
count = n
for i in range(n):
    if(arr[i] > h):
        count += 1
print(count)
