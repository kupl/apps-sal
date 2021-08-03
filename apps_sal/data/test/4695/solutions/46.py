x, y = map(int, input().split())
g = [[1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11]]
print("Yes" if any(x in g[i] and y in g[i] for i in range(2)) else "No")
