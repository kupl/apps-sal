n, l = map(int, input().split())
l1 = list(int(l) + i - 1 for i in range(1, n + 1))
n1 = sum(l1)
ans = min(l1, key=abs)

print(n1 - (ans))
