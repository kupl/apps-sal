n = int(input())
l = [int(i) for i in input().split()]
l = sorted(l)
ans = 0
for i in range(n // 2):
    ans = ans + ((l[i] + l[n - i - 1]) * (l[i] + l[n - i - 1]))
print(ans)
