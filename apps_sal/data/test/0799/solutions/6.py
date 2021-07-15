n = int(input())
a = list(map(int, input().split()))
m = max(a)
print(n * m - sum(a))
