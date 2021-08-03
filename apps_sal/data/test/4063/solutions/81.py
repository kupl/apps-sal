n = int(input())
p = list(map(int, input().split()))
nn = int(n / 2)
p.sort()
ans = p[nn] - p[nn - 1]

print(ans)
