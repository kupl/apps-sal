n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)
s = 0
for i in range(1, n):
    s += p[i // 2]
print(s)
