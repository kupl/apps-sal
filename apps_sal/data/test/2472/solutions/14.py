n = int(input())
x = [[0, 0]]
for _ in range(n):
    a, b = map(int, input().split())
    x.append([b, a])
x.sort()
for i in range(1, n + 1):
    x[i][1] += x[i - 1][1]
    if x[i][0] < x[i][1]:
        print("No")
        return
print("Yes")
