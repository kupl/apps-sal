n = int(input())
m1 = [0 for i in range(n)]
m2 = [0 for i in range(n)]
for i in range(n * n):
    (a, b) = list(map(int, input().split()))
    if m1[a - 1] == m2[b - 1] == 0:
        m1[a - 1] = m2[b - 1] = 1
        print(i + 1, end=' ')
