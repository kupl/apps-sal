(n, m) = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
print(max([min(i) for i in a]))
