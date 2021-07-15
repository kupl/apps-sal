n = int(input())


Max = 0
for i in range(0, n):
    k, j = map(int, input().split())
    Max = max(Max, k + j)


print(Max)
