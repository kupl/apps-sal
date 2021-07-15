n = int(input())
l = [*map(int, input().split())]
m = [e for e in l]
for i in range(n - 2, -1, -1):
    m[i] = max(0, min(m[i], m[i + 1] - 1))
print(sum(m))
