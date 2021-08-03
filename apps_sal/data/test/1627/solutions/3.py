n = int(input())
l = list(map(int, input().split()))

cmd = []
for i in range(n + 2):
    for j in range(n - 1):
        if l[j] > l[j + 1]:
            cmd.append([j + 1, j + 2])
            l[j], l[j + 1] = l[j + 1], l[j]
for x in cmd:
    print(*x)
