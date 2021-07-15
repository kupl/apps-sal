n = int(input())
l = [*map(int, input().split())]
def cost(x):
    x -= 1
    res = 0
    for i in range(n):
        res += l[i] * (abs(x - i) + abs(i - 0) + abs(0 - x))
    return res
res = float('inf')
for x in range(1, n + 1):
    res = min(res, cost(x))
print(2 * res)
