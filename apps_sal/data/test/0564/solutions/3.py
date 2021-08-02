n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
a.remove(max(a))
ans = sum(a) > s
print("NO" if ans else "YES")
