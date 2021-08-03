n = int(input())
p = [int(input()) for i in range(n)]
p = sorted(p, reverse=True)
result = p[0] // 2
for i in range(n - 1):
    result += p[i + 1]

print(result)
