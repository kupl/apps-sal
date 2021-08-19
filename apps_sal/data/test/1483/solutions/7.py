n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    p = [0] * n
    j = i
    while p[j] != 2:
        p[j] += 1
        j = l[j] - 1
    print(j + 1, end=' ')
