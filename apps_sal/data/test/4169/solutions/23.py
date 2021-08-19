(n, m) = [int(x) for x in input().split()]
a = sorted([[int(x) for x in input().split()] for _ in range(n)], key=lambda x: x[0])
result = 0
for x in a:
    cnt = min(m, x[1])
    result += x[0] * cnt
    m -= cnt
print(result)
