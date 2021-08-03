n = int(input())
res = [0, 0]
for _ in range(2 * n):
    l = [*map(int, input().split())]
    res[0] += l[0]
    res[1] += l[1]
print(res[0] // n, res[1] // n)
