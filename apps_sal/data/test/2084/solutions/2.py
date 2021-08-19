(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)
ans = sum(a[:k])
print(ans)
