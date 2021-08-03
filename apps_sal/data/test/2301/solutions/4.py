N = int(input())
List = [int(x) for x in input().split()]
List.sort()
count = 0
arr = [0] * N
index = 0
for i in range(1, N, 2):
    arr[i] = List[index]
    index += 1
for i in range(0, N, 2):
    arr[i] = List[index]
    index += 1
count = 0
for i in range(1, N - 1):
    if(arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
        count += 1
print(count)
print(*arr)
