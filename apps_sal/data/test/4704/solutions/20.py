n = int(input())
al = list(map(int, input().split()))

total = sum(al)
mn = abs(total - 2 * al[0])
x = 0
for i in range(1, n - 1):
    x += al[i - 1]
    y = total - x
    mn = min(mn, abs(x - y))

print(mn)
