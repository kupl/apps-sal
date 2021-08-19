(n, m, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
ans = min(sum((1 for i in a if i > x)), sum((1 for i in a if i < x)))
print(ans)
