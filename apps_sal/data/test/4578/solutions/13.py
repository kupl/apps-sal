n, k = map(int, input().split())
m = [int(input()) for _ in range(n)]
print(((k - sum(m))//min(m)) + n)
