x = list(map(int, input().split()))
n = int(x[0])
a = int(x[1])
b = int(x[2])

res = 0

for i in range(n + 1):
    m = sum([int(r) for r in list(str(i))])
    if a <= m <= b:
        res += i

print(res)
