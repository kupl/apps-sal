n, k = map(int, input().split())
print (max([x[0] - max(0, x[1] - k) for x in [list(map(int, input().split())) for i in range(n)]]))
