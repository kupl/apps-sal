n = int(input())
x = sorted(list(map(int, input().split())))
for i in range(n):
    print(x[i], x[2 * n - i - 1])
