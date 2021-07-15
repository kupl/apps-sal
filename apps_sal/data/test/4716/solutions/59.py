n, k = (int(x) for x in input().split())
L = [int(x) for x in input().split()]
ans = sum(sorted(L, reverse=True)[:k])
print(ans)
