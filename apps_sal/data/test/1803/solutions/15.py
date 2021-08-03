n = int(input())
arr = [0] + list(map(int, input().split())) + [0]
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1] += b - 1
    arr[a + 1] += arr[a] - b
    arr[a] = 0
print(*arr[1:-1], sep='\n')
