t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = []
    for i in range(0, n, 2):
        answer.append(-arr[i + 1])
        answer.append(arr[i])
    print(*answer)
