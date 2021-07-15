n, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for i in range(n)]
print(max([i[0] if k >= i[1] else i[0] - i[1] + k for i in arr]))
