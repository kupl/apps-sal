n, m = map(int, input().split())
print((n*max(n-1, 0)//2 + m*max(m-1, 0) // 2))
