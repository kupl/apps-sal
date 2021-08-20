n = int(input())
p = list(map(int, input().split()))
c = 0
for i in range(1, n - 1):
    s = [p[i - 1], p[i], p[i + 1]]
    if p[i] != min(s) and p[i] != max(s):
        c += 1
print(c)
