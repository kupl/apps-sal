n = int(input())
al = list(map(int, input().split()))
bl = list((i + 1 for i in range(n)))
cl = []
for (a, b) in zip(al, bl):
    cl.append(a - b)
cl.sort()
x = cl[n // 2]
ans = 0
for (a, b) in zip(al, bl):
    ans += abs(a - b - x)
print(ans)
