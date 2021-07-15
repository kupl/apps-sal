n = int(input())
x = [int(s) for s in input().split()]
a = []
for i in range(min(x), max(x) + 1):
    ans = 0
    for j in range(n):
        ans += (i - x[j]) ** 2
    a.append(ans)
print(min(a))
