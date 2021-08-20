(n, m) = map(int, input().split())
li1 = [0] * n
for i in range(m):
    (a, b) = map(int, input().split())
    li1[a - 1] += 1
    li1[b - 1] += 1
for i in range(n):
    print(li1[i])
