t = 1
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l = [0, 0]
    for i in range(n):
        if arr[i] % 2 != i % 2:
            l[i % 2] += 1
    if l[0] == l[1]:
        print(l[0])
    else:
        print(-1)
